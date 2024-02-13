import os
import re


class Twitter(object):
    version = '1.0'
    def __init__(self, backend=None):
        self.backend= backend
        self._tweets = []
    @property # getter for private class attribute
    def tweets(self):
        if self.backend and not self._tweets:
                self._tweets = [line.rstrip('\n') for line in self.backend.readlines()]
        return self._tweets

    def delete(self):
        if self.backend:
                os.remove(self.backend)

    def tweet(self, message):
        if len(message) > 160:
            raise Exception("Message too long.")
        self.tweets.append(message)
        if self.backend:
                self.backend.write("\n".join(self.tweets))

    def find_hashtags(self, message):
        return [m.lower() for m in re.findall("#(\w+)", message)]

if __name__ == '__main__':
    twitter = Twitter()
    print(twitter.version, twitter.tweets)
    twitter.tweet('This is a test message')
    print(twitter.tweets)