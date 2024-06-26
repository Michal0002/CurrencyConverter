import tkinter as tk
from services import converter

def convert_currency():
    global from_currency_var, to_currency_var, amount_entry, result_label

    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_entry.get()

    try:
        amount = float(amount)
        converted_amount = converter.convert(from_currency, to_currency, amount)
        result_label.config(text=f"{amount} {from_currency} is {round(converted_amount, 2)} {to_currency}")
    except ValueError:
        result_label.config(text="Invalid amount entered.")
    except Exception as e:
        result_label.config(text=str(e))

def main_menu():
    global from_currency_var, to_currency_var, amount_entry, result_label

    window = tk.Tk()
    window.title("Currency Converter")

    from_currency_var = tk.StringVar()
    from_currency_var.set("USD")
    to_currency_var = tk.StringVar()
    to_currency_var.set("EUR")

    currencies = sorted(converter.all_currencies())

    from_label = tk.Label(window, text="From Currency:")
    from_label.pack()
    from_menu = tk.OptionMenu(window, from_currency_var, *currencies)
    from_menu.pack()

    to_label = tk.Label(window, text="To Currency:")
    to_label.pack()
    to_menu = tk.OptionMenu(window, to_currency_var, *currencies)
    to_menu.pack()

    amount_label = tk.Label(window, text="Amount:")
    amount_label.pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    convert_button = tk.Button(window, text="Convert", command=convert_currency)
    convert_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    # Create a menu bar
    menubar = tk.Menu(window)
    window.config(menu=menubar)

    # Add Options menu
    options_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Display Data", command=display_data)

    window.mainloop()

def display_data():
    converter.display_data()
    
def about_info():
    messagebox.showinfo("About", "This is a simple currency converter application.")

if __name__ == "__main__":
    main_menu()
