from appJar import gui #uncomment this for 100% submission
import pandas
import tkinter #uncomment this for 100% submission

cart = []
total = 0

# Read data from CSV
df = pandas.read_csv("team_data.csv")
peripherals = df[df["Category"] == "Peripherals"].to_dict('records')
accessories = df[df["Category"] == "Accessories"].to_dict('records')
consoles = df[df["Category"] == "Consoles"].to_dict('records')
monitors = df[df["Category"] == "Monitors"].to_dict('records')

# Greet user and ask for a category
def greet_user():
    print("Welcome to our store!")
    while True:
        print("\nCategories: Peripherals, Accessories, Consoles, Monitors")
        category = input("What category would you like to browse? (Enter 'exit' to quit): ").lower()
        if category == "peripherals":
            browse_peripherals()
        elif category == "accessories":
            browse_accessories()
        elif category == "consoles":
            browse_consoles()
        elif category == "monitors":
            browse_monitors()
        elif category == "exit":
            checkout()
            break
        else:
            print("Invalid category. Please try again or type 'exit' to quit.")

# Function to browse peripherals
def browse_peripherals():
    global cart, total
    print("\nPeripherals:")
    for i, item in enumerate(peripherals):
        print(f"{i + 1}. {item['Item Name']} - ${item['Price (USD)']:.2f} (Stock: {item['Stock']})")
    choice = input("\nEnter the number of the item you'd like to add to your cart, or 'back' to return: ")
    if choice == "back":
        return
    else:
        for i in range(len(peripherals)):
            if choice == str(i + 1):
                if peripherals[i]["Stock"] > 0:
                    cart.append(peripherals[i]["Item Name"])
                    total += peripherals[i]["Price (USD)"]
                    peripherals[i]["Stock"] -= 1
                    print(f"\n{peripherals[i]['Item Name']} added to your cart for ${peripherals[i]['Price (USD)']:.2f}.")
                else:
                    print("\nSorry, that item is out of stock.")
                return
        print("\nInvalid choice. Please try again.")

# Function to browse accessories
def browse_accessories():
    global cart, total
    print("\nAccessories:")
    for i, item in enumerate(accessories):
        print(f"{i + 1}. {item['Item Name']} - ${item['Price (USD)']:.2f} (Stock: {item['Stock']})")
    choice = input("\nEnter the number of the item you'd like to add to your cart, or 'back' to return: ")
    if choice == "back":
        return
    else:
        for i in range(len(accessories)):
            if choice == str(i + 1):
                if accessories[i]["Stock"] > 0:
                    cart.append(accessories[i]["Item Name"])
                    total += accessories[i]["Price (USD)"]
                    accessories[i]["Stock"] -= 1
                    print(f"\n{accessories[i]['Item Name']} added to your cart for ${accessories[i]['Price (USD)']:.2f}.")
                else:
                    print("\nSorry, that item is out of stock.")
                return
        print("\nInvalid choice. Please try again.")

# Function to browse consoles
def browse_consoles():
    global cart, total
    print("\nConsoles:")
    for i, item in enumerate(consoles):
        print(f"{i + 1}. {item['Item Name']} - ${item['Price (USD)']:.2f} (Stock: {item['Stock']})")
    choice = input("\nEnter the number of the item you'd like to add to your cart, or 'back' to return: ")
    if choice == "back":
        return
    else:
        for i in range(len(consoles)):
            if choice == str(i + 1):
                if consoles[i]["Stock"] > 0:
                    cart.append(consoles[i]["Item Name"])
                    total += consoles[i]["Price (USD)"]
                    consoles[i]["Stock"] -= 1
                    print(f"\n{consoles[i]['Item Name']} added to your cart for ${consoles[i]['Price (USD)']:.2f}.")
                else:
                    print("\nSorry, that item is out of stock.")
                return
        print("\nInvalid choice. Please try again.")

# Function to browse monitors
def browse_monitors():
    global cart, total
    print("\nMonitors:")
    for i, item in enumerate(monitors):
        print(f"{i + 1}. {item['Item Name']} - ${item['Price (USD)']:.2f} (Stock: {item['Stock']})")
    choice = input("\nEnter the number of the item you'd like to add to your cart, or 'back' to return: ")
    if choice == "back":
        return
    else:
        for i in range(len(monitors)):
            if choice == str(i + 1):
                if monitors[i]["Stock"] > 0:
                    cart.append(monitors[i]["Item Name"])
                    total += monitors[i]["Price (USD)"]
                    monitors[i]["Stock"] -= 1
                    print(f"\n{monitors[i]['Item Name']} added to your cart for ${monitors[i]['Price (USD)']:.2f}.")
                else:
                    print("\nSorry, that item is out of stock.")
                return
        print("\nInvalid choice. Please try again.")

# Checkout and display the final cart
def checkout():
    global cart, total
    print("\nYour shopping session is complete!")
    if cart:
        print("\nHere are the items in your cart:")
        for item in cart:
            print(f"- {item}")
        tax = total * 0.09
        total_with_tax = total + tax
        print(f"\nSubtotal: ${total:.2f}")
        print(f"Tax (9%): ${tax:.2f}")
        print(f"Total (with tax): ${total_with_tax:.2f}")
        print("\nThank you for shopping with us!")
    else:
        print("\nYour cart is empty. Thank you for visiting!")

#commented according to the instructions
#greet_user()

#GUI Settings

def press(btn):
    if btn == "Peripherals":
        browse_peripherals()
    elif btn == "Accessories":
        browse_accessories()
    elif btn == "Consoles":
        browse_consoles()
    elif btn == "Monitors":
        browse_monitors()
    elif btn == "Checkout":
        checkout()
    elif btn == "Exit":
        app.stop()

app = gui("Pixel Palace", "800x800")

# Styled title
app.addLabel("title", "Welcome to Pixel Palace")
app.setLabelBg("title", "light blue")  
app.setLabelFg("title", "dark blue")  
app.setLabelFont("title", size=20, family="Helvetica")  
app.setPadding([5, 10])  


app.addImage("decor","Pixel Palace.gif")
app.setImageSize("decor", 400,400)


buttons = ["Peripherals", "Accessories", "Consoles", "Monitors", "Checkout", "Exit"]
for button in buttons:
    app.addButton(button, press)

for button in buttons:
    app.setButtonFont(button, size=14, family="Helvetica")
    app.setButtonFg(button, "black")


app.go()

