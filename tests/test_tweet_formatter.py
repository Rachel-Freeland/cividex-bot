import pytest
from cividex_bot.tweet_formatter import Formatter


def test_exists():
    assert Formatter

def test_formatting(fact_data):
    formatter = Formatter()
    actual = formatter.format_tweet(fact_data)
    expected = "Type of rights: Civil \nOn 1955-06-23: June 23 – Virginia Governor Thomas B. Stanley and Board of Education decide to continue segregated schools into 1956. \n Source: https://en.wikipedia.org/wiki/Timeline_of_the_civil_rights_movement"
    assert actual == expected


@pytest.fixture
def fact_data():
    return [    {
        "id": 13,
        "date": "1955-06-23",
        "flags": "c",
        "fact": "June 23 – Virginia Governor Thomas B. Stanley and Board of Education decide to continue segregated schools into 1956.",
        "source": "https://en.wikipedia.org/wiki/Timeline_of_the_civil_rights_movement",
        "progress": False,
        "verified": True,
        "contributor": 1
    },]