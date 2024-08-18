from unittest import TestCase
from polyend_tracker_pti_creator.utils.pti.pti import PTI

class TestInteg(TestCase):
    def test_integration(self) -> None:
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
                {
                    'source_path': '/Users/adriananders/polyend-tracker-pti-creator/tests/utils/files/integ',
                    'source_file_name': 'ss',
                    'source_extension': '.wav',
                    'destination_path': '/Users/adriananders/polyend-tracker-pti-creator/tests/utils/files/integ',
                    'destination_file_name': 'ss',
                    'destination_extension': '.pti',
                    'instrument_name': 'test'
                },
            ],
            'mode': 'normal',
            'playback': 'dynamic'
        }
        PTI(settings).create()