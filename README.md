# Introduction

Hello there,

This is my first Readme file for my **Capstone Project Module 1** from Purwadhika which I'm very excited to share. This project present the fundamentals of CRUD application, my first application made with Visual Code using Python language to write it. The application is a menu-ordering app in a cafe which I named, Norways_Cafe().

In this project, I've implemented several features such as:
 - Create: Adding an item (drink/food) to the menu list
 - Read: Display the menu list (drink/food) from the database
 - Update: Updating values (stock, price) of items from the database
 - Delete: Remove an item (food/drink) from the database

If there is a suggestion or recommendation, I'm very open to have a discussion with you guys which will improve me as a better Data Scientist. Thankss!!

Also, I hope my project can give you something useful for your programming journey

# A Menu-Ordering App, Norways_Cafe()
This project is to help the developer(me) for understanding the fundamentals of Python Prgoramming especially in CRUD (Create, Read, Update, Delete) concept by build an menu-ordering application. This application has several follwoing features:

## Description
**1. Product Catalog**
   - Displays Menu  : The application can displays the menu to the customer from dictionary-                        based database that consist primary key and values (name, stock, price, 
                      category) for each item whether drink or food menu
   - Filtered-result: The application can displays filtered-result menu to the customer based 
                      on his/her choice (by inputting) such as Coffee or Non-Coffee for the 
                      drinks menu and Main Course, Salty Snack, Sweet Snack for the foods menu.
     
**2. Order Management**
  - Add to Order List: The application add several customer's order using a list named,                                total_orders[]
  - Multiple Order: The application offers multiple order choice whether after customer     
                       ordered drink(s), he/she can keep ordering drink(s) or switch to     ordering food(s). When the cutomer ordered food(s), he/she can keep 
                       ordering food(s) or switch to ordering dring(s)

  **3. Billing System**
   - Calculate Bill: The application sum of all total orders quantity multiplied by its price The Billing system uses variable total_orders (to store all drinks_order and foods_order) and total_bills (sum of quantity multiplied with its price of all orders)
   - Printing the Bill: The application stores what customer order consist information such as name, Qty (quantity), price, and the total price. The application prints the Bill just like in a real-life scenario

  **4. Inventory Management**
  - Update value: The application can update values from the menu list such as stock and price using Admin System. And after orders take placed, the value (stock) of food or drink item, will also be updated
  
      

## Flowchart
You can see and download my flowchart below

[Flowchart Capstone_Module 1_Norways Cafe_9_Yusril.pdf](https://github.com/user-attachments/files/17107394/Flowchart.Capstone_Module.1_Norways.Cafe_9_Yusril.pdf)

# Code Explanation

## Database Preparation

First, we need to list our drinks and foods menu in form of dictionary that consist of key (1,2,3,...) and values (name, stock, and price). In this README I will only show  the drinks menu as an example,

```python
# Listing Drinks Menu
drinks_menu = {
    # Coffee
    1: {"name": "Es Kopi Susu Gula Aren", "stock": 50, "price": 18000, "category": "Coffee"},
    2: {"name": "Cappucino", "stock": 35, "price": 16000, "category": "Coffee"},
    3: {"name": "Caffe Latte", "stock": 25, "price": 17000, "category": "Coffee"},
    4: {"name": "Mochacino", "stock": 25, "price": 17000, "category": "Coffee"},
    5: {"name": "Espresso", "stock": 50, "price": 13000, "category": "Coffee"},
    6: {"name": "Caramel Latte", "stock": 25, "price": 17000, "category": "Coffee"},
    7: {"name": "Americano", "stock": 40, "price": 15000, "category": "Coffee"},
    8: {"name": "Caramel Latte", "stock": 25, "price": 17000, "category": "Coffee"},
    9: {"name": "Hazelnut Latte", "stock": 25, "price": 17000, "category": "Coffee"},
    # Non-Coffee
    10: {"name": "Matcha Latte", "stock": 30, "price": 18000, "category": "Non-Coffee"},
    11: {"name": "Taro Latte", "stock": 30, "price": 18000, "category": "Non-Coffee"},
    12: {"name": "Vanilla Latte", "stock": 27, "price": 19000, "category": "Non-Coffee"},
    13: {"name": "Matcha Frappe", "stock": 27, "price": 22000, "category": "Non-Coffee"},
    14: {"name": "Cookies N Cream Frappe", "stock": 25, "price": 22000, "category": "Non-Coffee"},
    15: {"name": "Butterscotch Sea Salt Latte", "stock": 25, "price": 22000, "category": "Non-Coffee"},
    16: {"name": "Buttercream Tiramisu Latte", "stock": 25, "price": 22000, "category": "Non-Coffee"},
    17: {"name": "Classic Tea", "stock": 40, "price": 12000, "category": "Non-Coffee"},
    18: {"name": "Earl Grey Tea", "stock": 40, "price": 12000, "category": "Non-Coffee"},
    19: {"name": "Lemon Tea", "stock": 40, "price": 12000, "category": "Non-Coffee"},
    20: {"name": "Mineral Water", "stock": 60, "price": 5000, "category": "Non-Coffee"}
}
```

## Defining the Variables
We need to define global variables to help us store multiple orders.
```python
# Declare global order lists and total bills

drink_orders = []    # To store all of the drink orders
food_orders = []     # To store all of the food orders
drink_bill = 0       # To sum all of the drink orders total price
food_bill = 0        # To sum all of the food orders total price
```
## Defining the Functions
Before running the application, we need to define each function in our code

## a) Main Menu
The main menu of the application is called function norways_cafe(). The function shows several choices such as display drink or food menu, buy drink or food menu, admin system menu, and exit program

### 1. norways_cafe()
```python
def norways_cafe():
    while True:
        print("\nWelcome to the Norway's Cafe")
        print("Menu List:")
        print("1. Displays the Drinks Menu")
        print("2. Displays the Foods Menu")
        print("3. Buy drinks")
        print("4. Buy foods")
        print("5. Admin")
        print("6. Exit Program")

        choice = input("Enter the menu number you want to run: ").lower().strip()

        if choice == '1':
            display_drinks_filter()
        elif choice == '2':
            display_foods_filter()
        elif choice == '3':
            buy_drinks()
        elif choice == '4':
            buy_foods()
        elif choice == '5':
            admin()
        elif choice == '6':
            print("\nThank you for visiting the Norway's Cafe!")
            break
        else:
            print("\nInvalid choice. Please try again.")
```

## Drinks Function
In this application, there are several drinks-related functions such as:
 1. display_drinks()  1     --> Function to display the list of drinks menu
 2. display_drinks_filter() -->  Function to display the list of drinks menu in a filtered way, Coffee or Non-Coffee
 3. add_drinks()            --> Function to add an item to the current drinks menu
 4. remove_drinks()         --> Function to add an item to the current drinks menu
 5. update_drinks()         --> Function to update values of an item (stock and price)

### 1. display_drinks()
```python
# Function to display the list of drinks menu
def display_drinks(category_filter=None):
    # Define the widths of each column based on the longest data in the list
    id_width = 5
    name_width = 35
    stock_width = 10
    price_width = 10
    
    # Calculate the total width of the menu title
    total_width = id_width + name_width + stock_width + price_width
    title_menu  = "Welcome to Norway's Cafe"

    # Print the menu title
    print("=" * total_width)
    print(title_menu.center(total_width))
    print("=" * total_width)

    # Print the header
    print(f"{'ID':<{id_width}}{'Drink':<{name_width}}{'Stock':<{stock_width}}{'Price':<{price_width}}")
    print("-" * (id_width + name_width + stock_width + price_width))

    # Print each drink item, applying the category filter 
    for drinks_id, drinks_info in drinks_menu.items():
        if category_filter is None or drinks_info['category'] == category_filter:
            name = drinks_info['name']
            stock = drinks_info['stock']
            price = drinks_info['price']
            print(f"{drinks_id:<{id_width}}{name:<{name_width}}{stock:<{stock_width}}{price:>{price_width},.2f}")
```

### display_drinks_filter()
```python
# Function to ask the customer for filtering the menu
def display_drinks_filter():
    display_drinks()  # Display all drinks initially

    # Ask the customer if they want to filter the menu
    while True:
        filter_choice = input("\nWould you like to filter the menu by category?: (yes/no)").lower()
        if filter_choice == "yes":
            print("\nCategories avalaible:")
            print("1. Coffee")
            print("2. Non-Coffee")

            category_choice = input("Please choose a category (coffee/non coffee)").lower().strip()

            if category_choice == "coffee":
                display_drinks("Coffee")
                print("\nDisplaying Coffee Menu")
            elif category_choice == "non coffee":
                display_drinks("Non-Coffee")
                print("\nDisplaying Non-Coffee Menu")
            else:
                print("\nInvalid choice. Please try again.")
            break
        elif filter_choice == "no":
            print("\nDisplaying full menu...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'")
```














