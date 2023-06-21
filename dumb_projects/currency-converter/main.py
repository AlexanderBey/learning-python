from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://free.curconv.com/"


BASE_URL = "http://free.currconv.com/"
API_KEY = "sample-key-do-not-use"

printer = PrettyPrinter()


def get_currencies():

    endpoint = f"api/v7/currencies?apiKey={API_KEY}" 
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())

    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = ['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "N/A")

        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()


    if len(data) == 0:
        print("Invalid currency")
        return
    
    rate = list(data.values()[0])
    print(f"1 {currency1} = {rate} {currency2}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    
    converted = amount * rate
    print(f"{amount} {currency1} = {converted} {currency2}")
    return converted


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    
    print("List - lists the different currencies")
    print("Convert - converts between two currencies")
    print("Rate - shows the exchange rate between two currencies")
    

    while True:
        command = input("Enter a command: (q to quit):").lower()

        if command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currence").upper()
            amount = input(f"Enter an amount of {currency1}")
            currency2 = input("Enter a target currency").upper()
            convert(currency1, currency2, amount)        
        elif command == "rate":
            currency1 = input("Enter a base currence").upper()
            currency2 = input("Enter a target currency").upper()
            exchange_rate(currency1, currency2)
        else: 
            print("Unknown command")