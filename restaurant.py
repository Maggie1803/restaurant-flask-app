from tkinter import *
import random
import time
from tkinter import messagebox

root = Tk()
root.geometry("1000x600")
root.title("Restaurant Management System")

# === Calculator Frame ===
operator = ""

def press(num):
    global operator
    operator += str(num)
    text_input.set(operator)

def clear():
    global operator
    operator = ""
    text_input.set("")

def equal():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = ""
    except:
        text_input.set("Error")
        operator = ""

text_input = StringVar()

# === Top Frame ===
Tops = Frame(root, width=1000, relief=SUNKEN)
Tops.pack(side=TOP)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=('Arial', 20, 'bold'), text="Restaurant Management System", fg="blue", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('Arial', 10), text=localtime, fg="black", anchor='w')
lblinfo.grid(row=1, column=0)

# === Left Frame ===
f1 = Frame(root, width=600, height=500, relief=SUNKEN)
f1.pack(side=LEFT)

# === Right Frame (Calculator) ===
f2 = Frame(root, width=400, height=500, relief=SUNKEN)
f2.pack(side=RIGHT)

# === Variables ===
order_no = StringVar()
fries = StringVar()
lunch = StringVar()
burger = StringVar()
pizza = StringVar()
cheese = StringVar()
drinks = StringVar()
cost = StringVar()
service = StringVar()
tax = StringVar()
subtotal = StringVar()
total = StringVar()

# === Price List ===
prices = {
    'Fries Meal': 25,
    'Lunch Meal': 40,
    'Burger Meal': 35,
    'Pizza Meal': 50,
    'Cheese Burger': 30,
    'Drinks': 35
}

def Ref():
    try:
        order_no.set(str(random.randint(10000, 99999)))
        f = int(fries.get() or 0) * prices['Fries Meal']
        l = int(lunch.get() or 0) * prices['Lunch Meal']
        b = int(burger.get() or 0) * prices['Burger Meal']
        p = int(pizza.get() or 0) * prices['Pizza Meal']
        c = int(cheese.get() or 0) * prices['Cheese Burger']
        d = int(drinks.get() or 0) * prices['Drinks']
        
        item_total = f + l + b + p + c + d
        serv_charge = round(item_total * 0.01, 2)
        tax_amt = round(item_total * 0.33, 2)
        total_cost = round(item_total + serv_charge + tax_amt, 2)

        cost.set(f"Rs. {item_total:.2f}")
        service.set(f"Rs. {serv_charge:.2f}")
        tax.set(f"Rs. {tax_amt:.2f}")
        subtotal.set(f"Rs. {item_total:.2f}")
        total.set(f"Rs. {total_cost:.2f}")
    except:
        messagebox.showerror("Error", "Enter only numbers!")

def reset():
    order_no.set("")
    fries.set("")
    lunch.set("")
    burger.set("")
    pizza.set("")
    cheese.set("")
    drinks.set("")
    cost.set("")
    service.set("")
    tax.set("")
    subtotal.set("")
    total.set("")
    clear()

def price_list_popup():
    price_window = Toplevel(root)
    price_window.title("Price List")
    price_window.geometry("250x200")
    Label(price_window, text="ITEM", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10)
    Label(price_window, text="PRICE", font=('Arial', 12, 'bold')).grid(row=0, column=1, padx=10)

    for i, (item, price) in enumerate(prices.items(), start=1):
        Label(price_window, text=item, font=('Arial', 10)).grid(row=i, column=0, sticky='w')
        Label(price_window, text=str(price), font=('Arial', 10)).grid(row=i, column=1, sticky='w')

# === Labels and Entries ===
Label(f1, text="Order No.", font=('Arial', 12, 'bold')).grid(row=0, column=0)
Entry(f1, textvariable=order_no, font=('Arial', 12)).grid(row=0, column=1)

Label(f1, text="Fries Meal", font=('Arial', 12, 'bold')).grid(row=1, column=0)
Entry(f1, textvariable=fries, font=('Arial', 12)).grid(row=1, column=1)

Label(f1, text="Lunch Meal", font=('Arial', 12, 'bold')).grid(row=2, column=0)
Entry(f1, textvariable=lunch, font=('Arial', 12)).grid(row=2, column=1)

Label(f1, text="Burger Meal", font=('Arial', 12, 'bold')).grid(row=3, column=0)
Entry(f1, textvariable=burger, font=('Arial', 12)).grid(row=3, column=1)

Label(f1, text="Pizza Meal", font=('Arial', 12, 'bold')).grid(row=4, column=0)
Entry(f1, textvariable=pizza, font=('Arial', 12)).grid(row=4, column=1)

Label(f1, text="Cheese burger", font=('Arial', 12, 'bold')).grid(row=5, column=0)
Entry(f1, textvariable=cheese, font=('Arial', 12)).grid(row=5, column=1)

Label(f1, text="Drinks", font=('Arial', 12, 'bold')).grid(row=0, column=2)
Entry(f1, textvariable=drinks, font=('Arial', 12)).grid(row=0, column=3)

Label(f1, text="Cost", font=('Arial', 12, 'bold')).grid(row=1, column=2)
Entry(f1, textvariable=cost, font=('Arial', 12)).grid(row=1, column=3)

Label(f1, text="Service Charge", font=('Arial', 12, 'bold')).grid(row=2, column=2)
Entry(f1, textvariable=service, font=('Arial', 12)).grid(row=2, column=3)

Label(f1, text="Tax", font=('Arial', 12, 'bold')).grid(row=3, column=2)
Entry(f1, textvariable=tax, font=('Arial', 12)).grid(row=3, column=3)

Label(f1, text="Subtotal", font=('Arial', 12, 'bold')).grid(row=4, column=2)
Entry(f1, textvariable=subtotal, font=('Arial', 12)).grid(row=4, column=3)

Label(f1, text="Total", font=('Arial', 12, 'bold')).grid(row=5, column=2)
Entry(f1, textvariable=total, font=('Arial', 12)).grid(row=5, column=3)

# === Buttons ===
Button(f1, text="PRICE", padx=16, pady=8, bd=10, fg="black", font=('Arial', 12), command=price_list_popup).grid(row=6, column=1)
Button(f1, text="TOTAL", padx=16, pady=8, bd=10, fg="black", font=('Arial', 12), command=Ref).grid(row=6, column=2)
Button(f1, text="RESET", padx=16, pady=8, bd=10, fg="black", font=('Arial', 12), command=reset).grid(row=6, column=3)
Button(f1, text="EXIT", padx=16, pady=8, bd=10, fg="black", font=('Arial', 12), command=root.quit).grid(row=6, column=4)

# === Calculator Buttons ===
txtDisplay = Entry(f2, font=('Arial', 20), textvariable=text_input, bd=10, insertwidth=2, width=14, justify='right')
txtDisplay.grid(columnspan=4)

btn_list = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
    ('0',4,0), ('c',4,1), ('=',4,2), ('/',4,3),
]

for (text, row, col) in btn_list:
    action = lambda x=text: clear() if x == 'c' else equal() if x == '=' else press(x)
    Button(f2, text=text, padx=16, pady=16, bd=8, fg="black", font=('Arial', 12, 'bold'), command=action).grid(row=row, column=col)

Label(f2, text="-By Amar Kumar", font=('Arial', 10)).grid(row=5, columnspan=4)

root.mainloop()
