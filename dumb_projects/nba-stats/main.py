from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://data.nba.net'
ALL_JSON = '/prod/v1/today.json'

response = get(BASE_URL + ALL_JSON).json()
pp = PrettyPrinter(response)

# file not yet started
# the goal is to get the json data from the nba api
# But i don't have an api key for the moment
