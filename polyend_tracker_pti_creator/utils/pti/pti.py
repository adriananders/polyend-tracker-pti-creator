import os
from typing import List, Dict
from pydub.audio_segment import AudioSegment
from polyend_tracker_pti_creator.utils.audio.audio import Audio
from polyend_tracker_pti_creator.utils.exceptions import (
    CreatorTooManyMergeFilesException,
    CreatorSampleTooLongException,
)
from polyend_tracker_pti_creator.utils.pti.header import Header
from polyend_tracker_pti_creator.utils.pti.constants import PLAYBACK_VALUES


class PTI:
    def __init__(self, settings: dict) -> None:
        self.files = settings['files']
        self.mode = settings['mode']
        self.playback = settings['playback']
        if self.mode == 'merge':
            self.merge_audio()
        else:
            self.get_audio()

    def merge_audio(self) -> None:
        if len(self.files) > 48:
            raise CreatorTooManyMergeFilesException(
                'Error! Too many files selected to merge into a single pti. Limited to 48 (maximum slices).'
            )
        combined = AudioSegment.empty()
        slice_points = [0]
        for file in self.files:
            audio = Audio(os.path.join(file['source_path'], file['source_file_name'] + file['source_extension']))
            combined += audio.audio_segment
            slice_points.append(slice_points[-1] + int(audio.audio_segment.frame_count()))
        slice_points.pop()
        combined_length = int(combined.frame_count())
        slice_points = [
            round((point / combined_length) * 65535) for point in slice_points
        ]
        self.files[0]['audio'] = combined
        self.files[0]['playback'] = self.playback
        self.files[0]['slice_points'] = slice_points
        self.files = [self.files[0]]

    def get_audio(self) -> None:
        for file in self.files:
            audio = Audio(os.path.join(file['source_path'], file['source_file_name'] + file['source_extension']))
            file['audio'] = audio.audio_segment
            if audio.loop_points != [0, 0]:
                file['loop_points'] = audio.loop_points
            if self.playback == 'dynamic':
                file['playback'] = 'forward-loop' if 'loop_points' in file else 'one-shot'
            else:
                file['playback'] = self.playback

    def create(self) -> None:
        for file in self.files:
            if len(file['audio']) > 30000:
                raise CreatorSampleTooLongException(
                    f"Error! File "
                    f"{os.path.join(file['source_path'], file['source_file_name'] + file['source_extension'])} "
                    f"is longer than 30 seconds (maximum .pti supported length)."
                )
            sample_length = self.get_sample_length(audio=file['audio'])
            settings = {
                'sample_length': sample_length,
                'instrument_name': file['instrument_name'],
                'sample_playback': PLAYBACK_VALUES[file['playback']]
            }
            if 'loop_points' in file:
                settings['loop_start'] = file['loop_points'][0]
                settings['loop_end'] = file['loop_points'][1]
            if 'slice_points' in file:
                settings = self.set_header_slice_points(settings=settings, slice_points=file['slice_points'])
            header = Header(settings)
            pti_data = header.data_bytes
            wav_bytes = file['audio'].raw_data
            pti_data.extend(wav_bytes)
            with open(os.path.join(
                    file['destination_path'],
                    file['destination_file_name'] +
                    file['destination_extension']
            ), mode='wb') as pti_file:
                pti_file.write(pti_data)

    @staticmethod
    def get_sample_length(audio: AudioSegment) -> int:
        return round((len(audio) / 1000) * 44100)

    @staticmethod
    def set_header_slice_points(settings: Dict, slice_points: List[int]) -> Dict:
        settings['number_of_slices'] = len(slice_points)
        for i, point in enumerate(slice_points):
            settings[f'slice_{str(i+1).zfill(2)}_adjust'] = point
        return settings
