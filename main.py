import menu_view as menu
from services import converter

def switch(choice):
    if choice == '1':
        return "PLN"
    elif choice == '2':
        return "EUR"
    elif choice == '3':
        return "USD"
    else:
        print("Unknown choice")
        return None

from_currency, to_currency = menu.display_menu()

from_currency_str = switch(from_currency)
to_currency_str = switch(to_currency)

if from_currency_str and to_currency_str:
    amount = float(input("Enter the amount to convert: "))
    converted_currency = converter.convert(from_currency_str, to_currency_str, amount)
    if converted_currency:
        print(f"Converted currency from {from_currency_str} to {to_currency_str} is {converted_currency} {to_currency_str}")
    else:
        print("Conversion failed.")
else:
    print("Invalid values.")
