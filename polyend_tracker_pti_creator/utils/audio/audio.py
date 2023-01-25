from typing import List
from pydub.audio_segment import AudioSegment
from lazy_property import LazyProperty
from polyend_tracker_pti_creator.utils.audio.wave_chunk_parser_extended import (
    RiffChunkExtended,
)
from polyend_tracker_pti_creator.utils.exceptions import (
    FfmpegNotInstalledException,
)


class Audio:
    def __init__(self, path: str) -> None:
        self.path = path

    @LazyProperty
    def loop_points(self) -> List[int]:
        with open(self.path, "rb") as file:
            try:
                frame_count = AudioSegment.from_file(self.path, '.wav').frame_count()
                riff_chunk = RiffChunkExtended.from_file(file)
                sample_chunk = riff_chunk.sub_chunks[RiffChunkExtended.CHUNK_SAMPLE]
                return [
                    round((sample_chunk.first_loop_start / frame_count) * 65535),
                    round((sample_chunk.first_loop_end / frame_count) * 65535)
                ]
            except KeyError:
                return [0, 0]

    @LazyProperty
    def audio_segment(self) -> AudioSegment:
        try:
            audio_segment = AudioSegment.from_file(self.path, '.wav')
            if audio_segment.frame_rate != 44100:
                audio_segment = audio_segment.set_frame_rate(44100)
            if audio_segment.channels != 1:
                audio_segment = audio_segment.set_channels(1)
            if audio_segment.sample_width != 2:
                audio_segment = audio_segment.set_sample_width(2)
            return audio_segment
        except FileNotFoundError as exception:
            if exception.filename == "ffprobe":
                raise FfmpegNotInstalledException(
                    "ffmpeg or libav is required to read audio from non-wave files. "
                    "Please download and install from ffmpeg.org or libav.org then try again."
                ) from exception
            return None
