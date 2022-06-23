from os import environ as env
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()


database_route = env['DJANGO_DATABASE']
token_route = env['DJANGO_TOKEN']
user_name= env['DJANGO_USER']
user_pass = env['DJANGO_PASSWORD']

class Helper:
    """
    A class to assist in retreiving items from a Django API
    """

    def __init__(self) -> None:
        self.client = requests.session()
        self.filter = []

    def retrieve_tweet(self):
        """
        Retrieves information from back end
        """
        login_data = {"username": user_name, "password": user_pass}

        response = requests.post(token_route, login_data)
        token = response.json()
        jwt = token["access"]
        headers = {"Authorization": ("Bearer " + jwt)}
        response = requests.get(database_route, headers=headers)

        return response.json()

    def request_parser(self, data):
        """
        Parses the Get request from an array to a dictionary for easier searching
        """
        for item in data:
            if item["verified"] is True:
                self.filter.append(item)
        return self.filter

    # TODO: Reimplement date

    def date_filter(self, data):
        """
        Filters through parsed data to collect
        """
        # set string to concat to
        date_filtered_facts = []

        # Get Today's Date - returns YYYY-MM-DD
        today = str(datetime.date.today())
        # Slice off the first 5 characters leaving MM-DD
        month_day = today[5:]

        for item in data:
            if item["date"][5:] == month_day:
                date_filtered_facts.append(item)

        return date_filtered_facts

