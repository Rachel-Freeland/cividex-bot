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
            data = data[0]
            # Grab flag for type of rights -= Done this way to potentailly account for possibility of using multi-flags
            flags = data['flags']
            if flags == 'c':
                self.flags.append('Civil')
            if flags == 'v':
                self.flags.append('Voting')
            if flags == 's':
                self.flags.append('Slavery')
            if flags == 'z':
                self.flags.append('Citizenship')
            flags = self.flags[0]

            fact = data['fact']
            source = data['source']
            date_ = data['date']

            tweet_content = f"Type of rights: {flags} \nOn {date_}: {fact} \n Source: {source}"
            print(tweet_content)
            return tweet_content          
