import unittest
import Morse

class TestMorseCode(unittest.TestCase):


    def test_text_to_morse(self):
        self.assertEqual(Morse.text_to_morse("tia"), "- .. .-")

    def test_morse_to_text(self):
        self.assertEqual(Morse.morse_to_text("- .. .-"), "tia")

    def test_invalid_text_to_morse(self):
        self.assertEqual(Morse.text_to_morse("$$%@!"), "# # # # #")

    def test_invalid_morse_to_text(self):
        self.assertEqual(Morse.morse_to_text("---. -.-.-.--.-. -....-"), "###")

    def test_encryption_insensitive(self):
        self.assertEqual(Morse.text_to_morse("hello"), ".... . .-.. .-.. ---")
        self.assertEqual(Morse.text_to_morse("HEllo"), ".... . .-.. .-.. ---")



if __name__ == '__main__': 
    unittest.main()