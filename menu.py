import tkinter as tk
from tkinter import messagebox
from services import converter

def convert_currency():
    global from_currency_var, to_currency_var, amount_entry

    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_entry.get()

    try:
        amount = float(amount)
        converted_amount = converter.convert(from_currency, to_currency, amount)
        messagebox.showinfo("Conversion Result", f"{amount} {from_currency} is {round(converted_amount, 2)} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main_menu():
    global from_currency_var, to_currency_var, amount_entry

    window = tk.Tk()
    window.title("Currency Converter")

    #default values
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

    window.mainloop()

if __name__ == "__main__":
    main_menu()
