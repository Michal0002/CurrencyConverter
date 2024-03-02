from currency_converter import CurrencyConverter
from datetime import datetime
from tabulate import tabulate
import pandas as pd

currency = CurrencyConverter()

def convert(from_currency, to_currency, amount):
    if not from_currency or not to_currency: 
        print ("Invalid currency")
    elif amount <= 0:
        print ("Amount must be positive")
    else:
        return currency.convert(amount, from_currency, to_currency)

def display_data():
    currencies = currency.currencies
    date = datetime.today().strftime('%Y-%m-%d')
    
    currency_data = [(currency, round(currency.convert(1, currency, 'USD'), 2), date) for currency in currencies]
    df = pd.DataFrame(currency_data, columns=['Currency', 'Value', "Date"])
    print(tabulate(df, headers='keys', tablefmt='rounded_outline', showindex=False))


def all_currencies():
    currencies = currency.currencies
    return currencies