from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="njQxnIDklb46BqJ6q26Yw0eOc"
csecret="dagvPdHLcMteIhFMBMMP6MJPb3EKFdFS69kp4z4lLTkRH2AfqO"
atoken="1150625820-aVjr7v9fKslufU4zHi3KmTTlUAFMF1xYJKIoW0d"
asecret="gQP3BkHhpNvIlzMwrqdmzZIiI2mgSfHaFjUtwcEHDDVHG"

class listener(StreamListener):
    counter = 0

    def on_data(self, data):
        self.counter += 1
        print(self.counter)
        f = open("tweet.txt", "a")
        f.write(data)
        f.close()
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["cloud"])
