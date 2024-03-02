from currency_converter import CurrencyConverter

def convert(from_currency, to_currency, amount):
    currency = CurrencyConverter()
    return currency.convert(amount, from_currency, to_currency)
