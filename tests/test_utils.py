import unittest
from utils.audio_utils import process_audio
from utils.music_utils import generate_music

class UtilsTestCase(unittest.TestCase):
    def test_process_audio(self):
        """Test the audio processing function."""
        try:
            result = process_audio('data/examples/sample_audio.wav')
            self.assertIsInstance(result, dict)  # Adjust based on expected output
        except Exception as e:
            self.fail(f"process_audio() raised an exception: {e}")

    def test_generate_music(self):
        """Test the music generation function."""
        try:
            music = generate_music()
            self.assertIsNotNone(music)
            self.assertIsInstance(music, bytes)  # Adjust based on expected output
        except Exception as e:
            self.fail(f"generate_music() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
