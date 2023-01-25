from typing import List, Dict
from argparse import Namespace
import os
import re
import pathlib
from lazy_property import LazyProperty
from polyend_tracker_pti_creator.utils.exceptions import (
    CreatorSourceMissingException,
    CreatorDestinationInvalidException,
    CreatorNoSourceWavFilesException,
    CreatorModeInvalidException,
    CreatorPlaybackInvalidException,
)

MODES = ['normal', 'merge']
PLAYBACK_TYPES = [
    'one-shot',
    'forward-loop',
    'backward-loop',
    'ping-pong-loop',
    'slice',
    'beat-slice',
    'wavetable',
    'granular',
    'dynamic',
]


class Settings:
    def __init__(self, args: Namespace) -> None:
        self.args = args
        for index, file in enumerate(self.files):
            file['destination_path'] = self.destination
            file['destination_file_name'] = f"{self.file_name.lower().replace('.pti', '')}" \
                                            f"{index + 1 if self.batch and self.mode != 'merge' else ''}" \
                if self.file_name else file['source_file_name']
            file['destination_extension'] = '.pti'
            if self.instrument_name:
                base_instrument_name = self.instrument_name
            else:
                base_instrument_name = file['source_file_name']
            base_instrument_name = re.sub(r'[^a-zA-Z0-9@ +-]', '', base_instrument_name)
            file['instrument_name'] = f"{base_instrument_name[0:32 - len(str(index + 1))]}{index + 1}" \
                if self.batch and self.instrument_name and self.mode != 'merge' else base_instrument_name[0:32]

        self.settings = {
            "files": self.files,
            "mode": self.mode,
            "playback": self.playback,
        }

    @LazyProperty
    def mode(self) -> str:
        mode = self.args.mode
        mode = mode if mode else 'normal'
        if mode not in MODES:
            raise CreatorModeInvalidException(
                "Error! Gave an invalid mode. Valid values are 'normal' and 'merge'."
            )
        return mode

    @LazyProperty
    def source(self) -> str:
        if not self.args.source:
            raise CreatorSourceMissingException(
                "Error! Please specify required --source (-s) argument."
            )

        if not os.path.exists(self.args.source):
            raise CreatorSourceMissingException(
                "Error! Please specify a valid source path."
            )
        return self.args.source

    @LazyProperty
    def destination(self) -> str:
        destination = self.args.destination
        if destination:
            if not os.path.exists(destination):
                raise CreatorDestinationInvalidException(
                    "Error! Please specify a valid destination path."
                )
        else:
            destination = self.source
        if os.path.isfile(destination):
            destination = os.path.dirname(destination)
        return destination

    @LazyProperty
    def instrument_name(self) -> str:
        return self.args.instrument_name \
            if self.args.instrument_name or not self.args.file_name \
            else self.args.file_name.lower().replace('.pti', '')

    @LazyProperty
    def file_name(self) -> str:
        file_name = self.args.file_name
        if file_name:
            return file_name
        return os.path.basename(self.source) if os.path.isfile(self.source) else None

    @LazyProperty
    def files(self) -> List[Dict[str, str]]:
        source_files = [self.source]
        if not os.path.isfile(self.source):
            source_files = os.listdir(self.source)
            source_files.sort()
            source_files = [os.path.join(self.source, file) for file in source_files]
        files = [
            {
                'source_path': os.path.dirname(file),
                'source_file_name': pathlib.Path(os.path.basename(file)).stem.lower(),
                'source_extension': pathlib.Path(os.path.basename(file)).suffix.lower()
            } for file in source_files if pathlib.Path(os.path.basename(file)).suffix.lower() == '.wav'
        ]

        if not files:
            raise CreatorNoSourceWavFilesException(
                "Error! No .wav files selected. Currently only .wav files supported. "
                "If you're trying to use non-wav files, please convert to .wav then try again."
            )
        return files

    @LazyProperty
    def playback(self) -> str:
        playback = self.args.playback
        if not playback:
            if self.mode == 'merge':
                playback = 'beat-slice'
            else:
                playback = 'dynamic'

        if playback not in PLAYBACK_TYPES:
            raise CreatorPlaybackInvalidException(
                "Error! Gave an invalid playback type. Valid values are 'one-shot', 'forward-loop', 'backward-loop', "
                "'ping-pong-loop', 'slice', 'beat-slice', 'wavetable', 'granular', and 'dynamic'"
            )
        return playback

    @LazyProperty
    def batch(self) -> bool:
        return len(self.files) > 1
