from datetime import date
import random


class Formatter():
    '''
    A class to assist in formatting tweets from API
    '''
    def __init__(self) -> None:
        self.flags = []

    def format_tweet(self, data):
        '''
        Takes data from backend and formats it into a tweet
        '''
        if data is None:
            cur_day_mon = str(date.today())[5:]
            string = f"We do not have anything for \n {cur_day_mon} in our database. "
            print(string)

        if len(data) >= 1:

            data = random.sample(data, 1)
            # Grab flag for type of rights -= Done this way to potentailly account for possibility of using multi-flags
            flags = data['flags']
            if 'c' in flags:
                self.flags.append('Civil')
            if 'v' in flags:
                self.flags.append('Voting')
            if 's' in flags:
                self.flags.append('Slavery')
            if 'z' in flags:
                self.flags.append('Citizenship')
            flags = self.flags[0]

            fact = data['facts']
            source = data['source']
            date_ = data['date']

            tweet_content = f"Type of rights: {flags} \n on {date_} {fact} \n Source: {source}"
            print(tweet_content)
            return tweet_content          
