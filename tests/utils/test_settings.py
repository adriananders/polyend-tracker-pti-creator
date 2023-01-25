from unittest import TestCase
from polyend_tracker_pti_creator.utils.settings import Settings
from polyend_tracker_pti_creator.utils.exceptions import (
    CreatorSourceMissingException,
    CreatorNoSourceWavFilesException,
    CreatorDestinationInvalidException,
    CreatorModeInvalidException,
    CreatorPlaybackInvalidException,
)


class TestObject:
    def __init__(self, settings):
        self.source = settings['source']
        self.destination = settings['destination'] if 'destination' in settings else None
        self.file_name = settings['file_name'] if 'file_name' in settings else None
        self.instrument_name = settings['instrument_name'] if 'instrument_name' in settings else None
        self.mode = settings['mode'] if 'mode' in settings else None
        self.playback = settings['playback'] if 'playback' in settings else None


class TestSettings(TestCase):
    def test_no_source(self) -> None:
        args = TestObject({'source': None})
        with self.assertRaises(CreatorSourceMissingException) as context:
            Settings(args)
            self.assertTrue('Error! Please specify required --source (-s) argument.' in context.exception)

    def test_invalid_source(self) -> None:
        args = TestObject({'source': 'testpath'})
        with self.assertRaises(CreatorSourceMissingException) as context:
            Settings(args)
            self.assertTrue('Error! Please specify a valid source path.' in context.exception)

    def test_no_wav_files_source(self) -> None:
        args = TestObject({'source': './'})
        with self.assertRaises(CreatorNoSourceWavFilesException) as context:
            Settings(args)
            self.assertTrue("Error! No .wav files selected. Currently only .wav files supported. "
                            "If you're trying to use non-wav files, please convert to .wav then try again."
                            in context.exception)

    def test_invalid_destination(self) -> None:
        args = TestObject({
            'source': './tests/utils/files',
            'destination': 'invalidpath'
        })
        with self.assertRaises(CreatorDestinationInvalidException) as context:
            Settings(args)
            self.assertTrue("Error! Please specify a valid destination path." in context.exception)

    def test_merge_config(self) -> None:
        args = TestObject({
            'source': './tests/utils/files',
            'destination': './tests/utils/files/tone.wav',
            'file_name': 'test',
            'instrument_name': 'test',
            'mode': 'merge',
            'playback': None,
        })

        self.assertEqual(Settings(args).settings, {
            'files': [
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'test_tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                },
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                }, {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone2',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                }
            ],
            'mode': 'merge',
            'playback': 'beat-slice'
        })

    def test_instrument_name(self) -> None:
        args = TestObject({
            'source': './tests/utils/files',
            'destination': None,
            'file_name': None,
            'instrument_name': 'test',
            'mode': None,
            'playback': None,
        })
        self.assertEqual(Settings(args).settings, {
            'files': [
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'test_tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test_tone',
                    'destination_extension': '.pti',
                    'instrument_name': 'test1'
                },
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone',
                    'destination_extension': '.pti',
                    'instrument_name': 'test2'
                }, {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone2',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone2',
                    'destination_extension': '.pti',
                    'instrument_name': 'test3'
                }
            ],
            'mode': 'normal',
            'playback': 'dynamic'
        })

    def test_file_name(self) -> None:
        args = TestObject({
            'source': './tests/utils/files',
            'destination': './tests/utils/files',
            'file_name': 'test',
            'instrument_name': None,
            'mode': None,
            'playback': None,
        })
        self.assertEqual(Settings(args).settings, {
            'files': [
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'test_tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test1',
                    'destination_extension': '.pti',
                    'instrument_name': 'test1'
                },
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test2',
                    'destination_extension': '.pti',
                    'instrument_name': 'test2'
                }, {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone2',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'test3',
                    'destination_extension': '.pti',
                    'instrument_name': 'test3'
                }
            ],
            'mode': 'normal',
            'playback': 'dynamic'
        })

    def test_invalid_mode(self) -> None:
        args = TestObject({
            'source': './tests/utils/files',
            'destination': None,
            'file_name': 'test',
            'instrument_name': None,
            'mode': 'test',
            'playback': None,
        })
        with self.assertRaises(CreatorModeInvalidException) as context:
            Settings(args)
            self.assertTrue("Error! Gave an invalid mode. Valid values are 'normal' and 'merge'." in context.exception)

    def test_invalid_playback(self) -> None:
        args = TestObject({
            'source': './tests/utils/files',
            'destination': None,
            'file_name': 'test',
            'instrument_name': None,
            'mode': None,
            'playback': 'test',
        })
        with self.assertRaises(CreatorPlaybackInvalidException) as context:
            Settings(args)
            self.assertTrue("Error! Gave an invalid playback type. Valid values are 'one-shot', "
                            "'forward-loop', 'backward-loop', "
                            "'ping-pong-loop', 'slice', 'beat-slice', 'wavetable', "
                            "'granular', and 'dynamic'" in context.exception
                            )
