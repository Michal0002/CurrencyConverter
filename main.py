import menu_view as menu

def switch(choice):
    if choice == '1':
        print("PLN")
    elif choice == '2':
        print("EUR")
    elif choice == '3':
        print("USD")
    else:
        print("Unknown choice")

from_currency, to_currency = menu.display_menu()

switch(from_currency)
