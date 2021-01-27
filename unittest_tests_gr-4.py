import unittest
import sentenceVerification


class TestSentence(unittest.TestCase):
    # Test if there's an uppercase at the start of the string
    def test_firstLetterUpperCase(self):
        self.assertTrue(sentenceVerification.sentenceVerification("Ceci est une phrase."))
        self.assertFalse(sentenceVerification.sentenceVerification("ceci est une phrase."))

    # Test if the number of words is between 2 and 10 excluded
    def test_numberOfWords(self):
        self.assertFalse(sentenceVerification.sentenceVerification("Ceci est."))
        self.assertTrue(sentenceVerification.sentenceVerification("Ceci est une phrase."))
        self.assertFalse(sentenceVerification.sentenceVerification("Ceci est une grande phrase trop longue pour être valide."))

    # Test if there's a period at the end of the sentence
    def test_periodAtEnd(self):
        self.assertTrue(sentenceVerification.sentenceVerification("Ceci est une phrase."))
        self.assertFalse(sentenceVerification.sentenceVerification("Ceci est une phrase"))


if __name__ == '__main__':
    unittest.main()
