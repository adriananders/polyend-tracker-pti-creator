from unittest import TestCase
from polyend_tracker_pti_creator.utils.pti.header import Header
from polyend_tracker_pti_creator.utils.pti.constants import PTI_HEADER_DEFINITION


class TestHeader(TestCase):
    def test_format(self) -> None:
        header = Header({})
        self.assertEqual(
            '<2sBBBBBBBBBBBBBBBBBB?32sBBBBBBB'
            'LHBBHBBBBBBBBHHHHBBHBBfBBHBBHfHBB'
            'fBBHBBHfHBBfBBHBBHfHBBfBBHBBHfHBB'
            'fBBHBBHfHBBfBBHBBHfHBBBBBBfBBBBfB'
            'BBBfBBBBfBBBBfBBBBfffBBbbBBBBBBBB'
            'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
            'HHHHHHHHHHHHHHHBBHHBBBBBBBBBB',
            header.format
        )

    def test_data(self) -> None:
        header = Header({})
        self.assertEqual(len(PTI_HEADER_DEFINITION.keys()), len(header.data))

    def test_data_bytes(self) -> None:
        header = Header({
                'sample_length': 926110,
                'sample_playback': 0,
                'panning_env_attack': 3000,
                'cutoff_env_attack': 3000,
                'wt_pos_env_attack': 3000,
                'gran_pos_env_attack': 3000,
                'finetune_env_attack': 3000,
            })
        with open('./tests/utils/files/default_header.pti', mode='rb') as header_file:
            expected = bytearray(header_file.read())
            self.assertEqual(expected, header.data_bytes)
