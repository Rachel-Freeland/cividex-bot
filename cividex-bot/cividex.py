from os import environ as env
from dotenv import load_dotenv
import tweepy
from tweet_formatter import Formatter
from retrieve_tweet import Helper

formatter = Formatter()
helper = Helper()


load_dotenv()

# Set Variables for .env
consumer_key = env['CONSUMER_KEY']
consumer_secret = env['CONSUMER_KEY_SECRET']
access_token = env ['ACCESS_TOKEN']
access_token_secret = env ['ACCESS_TOKEN_SECRET']


#Twitter Authentication
def authenticate():
    '''
    Authenticates bot with twitter server allowing for access to tweets. 
    '''
    try: 
        auth = tweepy.OAuthHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        return tweepy.API(auth)
    except Exception as error:
        print(f'Unable to access and authenticate twitter API. Reason: {error}')


# Main runtime
def main():
    api = authenticate()
    # api.update_status('Hello World')

    tweet = helper.retrieve_tweet()
    tweet = formatter.format_tweet(tweet)
    tweet_content = tweet

    try:
        api.update_status(status=tweet_content)
        print('tweet has been tweeted')
    except Exception as error:
        print(f"An error occurred while tweeting. Reason: {error}")
  

if __name__ == "__main__":
    main()