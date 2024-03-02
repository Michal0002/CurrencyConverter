from services import converter

def mainMenu():
        print("\nCurrency Conventer")
        print("===================")
        choice = input("""
                        A: Convert currency
                        B: Display statistics
                        C: Exit
                        
                        Please enter your choice: """)

        if choice =="A" or choice == "a":
            optionA()            
        elif choice == "B" or choice == "b":
            converter.display_data()
            mainMenu()
        elif choice == "C" or choice == "c":
            print("Bye!")
            exit()
        else: 
            print("Invalid choice. Choose from available options.")
            mainMenu()


def display_menu():
    print("Choose your currency:")
    print("\n1. PLN")
    print("2. EUR")
    print("3. USD")
    from_currency = input("From: ")

    print("\n1. PLN")
    print("2. EUR")
    print("3. USD")
    to_currency = input("To: ")

    return from_currency, to_currency

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

def optionA():
    from_currency, to_currency = display_menu()  
    currency_converter = converter.CurrencyConverter() 

    from_currency_str = switch(from_currency)  
    to_currency_str = switch(to_currency)

    if from_currency_str and to_currency_str:
        amount = float(input("Enter the amount to convert: "))
        converted_currency = currency_converter.convert(amount, from_currency_str, to_currency_str)
        if converted_currency:
            print(f"Converted currency from {amount} {from_currency_str} is {converted_currency} {to_currency_str} ")
        else:
            print("Conversion failed.")
    else:
        print("Invalid values.")
