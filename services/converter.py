from currency_converter import CurrencyConverter
from datetime import datetime
from tabulate import tabulate
import pandas as pd
import tkinter as tk
from tkinter import messagebox


currency = CurrencyConverter()

def convert(from_currency, to_currency, amount):
    if not from_currency or not to_currency: 
        print ("Invalid currency")
    elif amount <= 0:
        print ("Amount must be positive")
    else:
        return currency.convert(amount, from_currency, to_currency)

def display_data():
    currencies = currency.currencies  # Pobieramy obiekty walut zamiast kodów walut
    date = datetime.today().strftime('%Y-%m-%d')
    try:
        currency_data = [(curr, round(currency.convert(1, curr, 'USD'), 2), date) for curr in currencies]
        df = pd.DataFrame(currency_data, columns=['Currency', 'Value', "Date"])
        messagebox.showinfo("Currency Data", df.to_string())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def all_currencies():
    currencies = currency.currencies
    return currencies