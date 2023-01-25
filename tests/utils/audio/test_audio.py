import os
from unittest import TestCase
from polyend_tracker_pti_creator.utils.audio.audio import (
    Audio,
)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

FILE_PATHS = [
    os.path.join(DIR_PATH, "../files/tone.wav"),
    os.path.join(DIR_PATH, "../files/tone2.wav"),
]


class TestAudio(TestCase):
    def test_audio_file(self) -> None:
        audio = Audio(FILE_PATHS[0])
        self.assertEqual(audio.loop_points, [13968, 65532])
        self.assertEqual(audio.audio_segment.frame_rate, 44100)
        self.assertEqual(audio.audio_segment.channels, 1)
        self.assertEqual(audio.audio_segment.frame_width, 2)
        audio2 = Audio(FILE_PATHS[1])
        self.assertEqual(audio2.loop_points, [0, 0])
