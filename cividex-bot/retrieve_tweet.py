from os import environ as env
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()


class Helper():
    '''
    A class to assist in retreiving items from a Django API
    '''
    def __init__(self) -> None:
        self.client = requests.session()
        self.filter = []


    def retrieve_tweet(self):
        '''
        Retrieves information from back end
        '''
        #TODO: LOGIN URL IN ENV
        url = 'https://cividex.herokuapp.com/api/token/'
        #TODO: USERNAME AND PASSWORD ENV
        login_data = {'username':'admin','password':'admin'}
        response = requests.post(url, login_data)
        token = response.json()
        jwt = token['access']

        headers = {
        'Authorization': ('Bearer ' + jwt)
    }
        #TODO : Add django /api/ route to ENV
        fact_url = 'https://cividex.herokuapp.com/api/v1/facts/'
        response = requests.get(fact_url, headers=headers)

        return self.request_parser(response.json())

    def request_parser(self, data):
        '''
        Parses the Get request from an array to a dictionary for easier searching
        '''
        for item in data:
            if item['verified'] is True:
                self.filter.append(item)
        return self.date_filter(self.filter)

    def date_filter(self, data):
        '''
        Filters through parsed data to collect 
        '''
        # set string to concat to
        date_filtered_facts = []
        
        # Get Today's Date - returns YYYY-MM-DD
        today = str(datetime.date.today())
        # Slice off the first 5 characters leaving MM-DD
        month_day = today[5:]

        for item in data:
            if item['date'][5:] == month_day:
                date_filtered_facts.append(item)

        return date_filtered_facts



    #TODO: Delete random parser used for testing
    # def request_parser(self, data):
    #     '''
    #     Parses the Get request from an array to a dictionary for easier searching
    #     '''

    #     for item in data:
    #         if item['verified'] is False:
    #             for key in item.keys():
    #             #TODO: Add query string and uncomment line below 
    #                 #if item[key] == query

    #                 self.filter.append(item)
    #     fact = random.sample(self.filter, 1)
    #     return fact[0]
