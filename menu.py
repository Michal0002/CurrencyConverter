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
    currencies = converter.all_currencies()    
    print("Choose your currency (FROM):")

    for idx, currency in enumerate(currencies, start=1):
        print(f"{idx}. {currency}")
    from_currency = input("From: ")
    
    print("\nChoose your currency (TO):")
    for idx, currency in enumerate(currencies, start=1):
        print(f"{idx}. {currency}")
    to_currency = input("To: ")
  
    return from_currency, to_currency    

def switch(choice):
    currencies = converter.all_currencies()
    if choice.isdigit() and 1 <= int(choice) <= len(currencies):
        return list(currencies)[int(choice) - 1]
    elif choice in currencies:
        return choice
    else:
        print("Unknown choice")
        return None

def optionA():
    from_currency, to_currency = display_menu()  
    currency_converter = converter.CurrencyConverter() 

    from_currency_str = switch(from_currency)  
    to_currency_str = switch(to_currency)

    if from_currency_str and to_currency_str:
        try:
            amount = float(input("Enter the amount to convert: "))
            converted_currency = currency_converter.convert(amount, from_currency_str, to_currency_str)
            print(f"Converted currency from {amount} {from_currency_str} is {round(converted_currency,2)} {to_currency_str}")
        except ValueError:
            print("Invalid amount entered.")
    else:
        print("Invalid currencies selected.")

    