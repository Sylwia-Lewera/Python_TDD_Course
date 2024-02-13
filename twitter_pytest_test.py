# run 'pip install pytest' to install pytest
import pytest

from twitter import Twitter

@pytest.fixture
def backend(tmpdir):
    temp_file=tmpdir.join('test.txt')
    temp_file.write('')
    return temp_file
@pytest.fixture(params=['list', 'backend'], name='twitter')  # fixture scope is global, for all tests (default scope = function)
def fixture_twitter(backend, request):
    if request.param == 'list':
        twitter = Twitter()
    elif request.param == 'backend':
        twitter = Twitter(backend=backend)
    return twitter

def test_twitter_initialization(twitter):
    assert twitter


def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):  # assertion for exception raised
        twitter.tweet('test' * 41)
    assert twitter.tweets == []


# Python decorator
@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first Test message", ["first"]),
        ("#FIRST Test message", ["first"]),
        ("Test message #first", ["first"]),
        ("Test message #first #second", ["first", "second"])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected

def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')
    assert twitter2.tweets == ['Test 1', 'Test 2']
