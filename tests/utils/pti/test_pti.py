import struct
from unittest import TestCase
from polyend_tracker_pti_creator.utils.pti.pti import PTI
from polyend_tracker_pti_creator.utils.pti.header import Header


class TestPTI(TestCase):
    def test_simple_single_forward_loop(self) -> None:
        settings = {
            'files': [
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                },
            ],
            'mode': 'normal',
            'playback': 'dynamic'
        }
        PTI(settings).create()
        with open('./tests/utils/files/tone.pti', mode='rb') as file:
            file_content = file.read()
            header = Header({
                'instrument_name':  'test',
                'sample_length': 21344,
                'sample_playback': 1,
                'loop_start': 13968,
                'loop_end': 65532,
            })
            actual_header_data = struct.unpack(header.format, file_content[:392])
            expected_header_data = header.data
            self.assertEqual(expected_header_data, actual_header_data)

    def test_merge_slice(self) -> None:
        settings = {
            'files': [
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone_slice',
                    'destination_extension': '.pti',
                    'instrument_name': 'testslice'
                },
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone2',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone_slice',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                },
            ],
            'mode': 'merge',
            'playback': 'beat-slice'
        }
        PTI(settings).create()
        with open('./tests/utils/files/tone_slice.pti', mode='rb') as file:
            file_content = file.read()
            header = Header({
                'instrument_name':  'testslice',
                'sample_length': 42689,
                'sample_playback': 5,
                'number_of_slices': 2,
                'slice_02_adjust': 32768
            })
            actual_header_data = struct.unpack(header.format, file_content[:392])
            expected_header_data = header.data
            self.assertEqual(expected_header_data, actual_header_data)

    def test_multi_single_one_shot(self) -> None:
        settings = {
            'files': [
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone_os_1',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                },
                {
                    'source_path': './tests/utils/files',
                    'source_file_name': 'tone2',
                    'source_extension': '.wav',
                    'destination_path': './tests/utils/files',
                    'destination_file_name': 'tone_os_2',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                },
            ],
            'mode': 'normal',
            'playback': 'one-shot'
        }
        PTI(settings).create()
        with open('./tests/utils/files/tone_os_1.pti', mode='rb') as file:
            file_content = file.read()
            header = Header({
                'instrument_name':  'test',
                'sample_length': 21344,
                'loop_start': 13968,
                'loop_end': 65532,
            })
            actual_header_data = struct.unpack(header.format, file_content[:392])
            expected_header_data = header.data
            self.assertEqual(expected_header_data, actual_header_data)
        with open('./tests/utils/files/tone_os_2.pti', mode='rb') as file:
            file_content = file.read()
            header = Header({
                'instrument_name':  'test',
                'sample_length': 21344,
                'loop_start': 1,
                'loop_end': 65534,
            })
            actual_header_data = struct.unpack(header.format, file_content[:392])
            expected_header_data = header.data
            self.assertEqual(expected_header_data, actual_header_data)
