import pytest
from cividex_bot.retrieve_tweet import Helper


def test_exists():
    assert Helper

def test_parser(fact_data):
    helper = Helper()
    actual = helper.request_parser(fact_data)
    expected = [    {
        "id": 13,
        "date": "1955-06-23",
        "flags": "c",
        "fact": "June 23 – Virginia Governor Thomas B. Stanley and Board of Education decide to continue segregated schools into 1956.",
        "source": "https://en.wikipedia.org/wiki/Timeline_of_the_civil_rights_movement",
        "progress": False,
        "verified": True,
        "contributor": 1
    },]
    assert actual == expected

















@pytest.fixture
def fact_data():
    return [    
        {
        "id": 12,
        "date": "1940-06-22",
        "flags": "c",
        "fact": "GI Bill",
        "source": "",
        "progress": False,
        "verified": False,
        "contributor": 1
    },
    {
        "id": 13,
        "date": "1955-06-23",
        "flags": "c",
        "fact": "June 23 – Virginia Governor Thomas B. Stanley and Board of Education decide to continue segregated schools into 1956.",
        "source": "https://en.wikipedia.org/wiki/Timeline_of_the_civil_rights_movement",
        "progress": False,
        "verified": True,
        "contributor": 1
    },
    {
        "id": 14,
        "date": "1940-06-22",
        "flags": "c",
        "fact": "GI Bill3",
        "source": "",
        "progress": False,
        "verified": False,
        "contributor": 1
    },]