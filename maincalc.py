from kalkulator import *
import requests
import json
import numpy as np
import pandas as pd 
    
root = Tk()
# Variables for currencies values
variable1 = StringVar(root)
variable2 = StringVar(root)
# Variable inicialization
variable1.set("currency")
variable2.set("currency")
# Currencies list, but is possibility to use all currencies available in API
CurrenyCode_list = ["PLN", "USD", "CAD", "RUB", "EUR", "BTC"]

def CurrencyConversion():
    """Real time currency converter"""
    from_currency = variable1.get()
    to_currency = variable2.get()
    url = f'https://api.exchangerate.host/convert?from={str(from_currency)}&to={str(to_currency)}'

    try:
        req_ob = requests.get(url)
        status_code = 200
    except: 
        status_code = 1000
    
    if status_code == 1000:
        with open('currencies.json', 'r') as f:
            data = json.load(f)
            pln = data[to_currency]
            
            print(data)
 
    else:
        result = req_ob.json()
        exchange_Rate = float(result['info']['rate'])
        amount = float(Amount1.get())
        new_amount = round(amount * exchange_Rate, 3)
        Amount2.insert(0, str(new_amount))
        with open('currencies.json', 'w') as json_file:  
            url = r'https://api.exchangerate.host/latest?base=PLN'
            req = requests.get(url)
            data = req.json()
            data = data['rates']
            json.dump(data, json_file)
            
def clear_all():
    Amount1.delete(0, END)
    Amount2.delete(0, END)

if __name__ == "__main__": 

    root.configure(background = 'light green')
    root.geometry("600x375")
    root.resizable(height=False, width=False)
    
    # Labels to inform users about entity
    headlabel = Label(root, text = 'Kalkulator walut',
                    fg = 'black', bg = "red")

    label1 = Label(root, text = "Wartość :",
                fg = 'black', bg = 'dark green')
    
    label2 = Label(root, text = "Z waluty  :",
                fg = 'black', bg = 'dark green')

    label3 = Label(root, text = "Na walute :",
                fg = 'black', bg = 'dark green')

    label4 = Label(root, text = "Przekonwertowana wartość :",
                fg = 'black', bg = 'dark green')

    # Labels mesh
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0)
    label2.grid(row = 2, column = 0)
    label3.grid(row = 3, column = 0)
    label4.grid(row = 5, column = 0)
    
    #Wartości  w aplikacji.
    Amount1 = Entry(root)
    Amount2 = Entry(root)
    Amount1.grid(row = 1, column = 1, ipadx ="25")
    Amount2.grid(row = 5, column = 1, ipadx ="25")

    #Lista walut
    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)
    
    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10)
    ToCurrency_option.grid(row = 3, column = 1, ipadx = 10)
    
    #przycisk do konwersji
    button1 = Button(root, text = "Convert", bg = "red", fg = "black",
                                command = CurrencyConversion)
    
    button1.grid(row = 4, column = 1)

    #Przycisk do wyczyszczenia
    button2 = Button(root, text = "Clear", bg = "red",
                    fg = "black", command = clear_all)
    button2.grid(row = 6, column = 1)

    # Start  GUI
    root.mainloop()
