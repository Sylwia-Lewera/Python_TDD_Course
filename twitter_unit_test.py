import unittest

from twitter import Twitter
class TwitterTest(unittest.TestCase):
    def setUp(self):
        # method called before each test
        self.twitter = Twitter()
    def test_initialization(self): #every method beginning with "test" is our unit test
        self.assertTrue(self.twitter)
    def test_tweet_single(self):
        # Given
        self.twitter = Twitter()
        # When
        self.twitter.tweet('Test message')
        # Then
        self.assertEqual(self.twitter.tweets, ['Test message'])


#good practice - function calls on file level (won't be trigerred by imports)
if __name__ == '__main__':
    unittest.main()
