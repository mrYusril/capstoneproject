# Section Listing the Menu
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

# Listing Foods Menu
foods_menu = {
    # Main_Course 
    1: {"name": "Chicken 'Tender' Burger", "stock": 40, "price": 23000, "category": "Main Course"},
    2: {"name": "Classic Beef Burger", "stock": 38, "price": 26000, "category": "Main Course"},
    3: {"name": "Western Beefbac Cheeseburger", "stock": 32, "price": 33000, "category": "Main Course"},
    4: {"name": "Memphis BBQ Burger", "stock": 32, "price": 33000, "category": "Main Course"},
    5: {"name": "Nasi Ayam Sambal Matah", "stock": 45, "price": 23000, "category": "Main Course"},
    6: {"name": "Nasi Ayam Sambal Kemangi", "stock": 45, "price": 23000, "category": "Main Course"},
    7: {"name": "Japanese Curry Rice", "stock": 42, "price": 24000, "category": "Main Course"},
    8: {"name": "Pesto Rice Chicken Katsu", "stock": 42, "price": 25000, "category": "Main Course"},
    9: {"name": "Tomato Mozzarella Rice", "stock": 40, "price": 25000, "category": "Main Course"},
    10: {"name": "Butter Rice Creamy Katsu", "stock": 60, "price": 25000, "category": "Main Course"},
    11: {"name": "Creamy Tomatto Mozzarella Rize", "stock": 55, "price": 25000, "category": "Main Course"},
    12: {"name": "Broccoli and Cheese", "stock": 55, "price": 24000, "category": "Main Course"},
    13: {"name": "Tomahawk Steak", "stock": 25, "price": 60000, "category": "Main Course"},
    14: {"name": "Tenderloin Steak", "stock": 28, "price": 42000, "category": "Main Course"},
    15: {"name": "Striploin Steak", "stock": 28, "price": 42000, "category": "Main Course"},
    16: {"name": "Crispy Chicken Steak", "stock": 35, "price": 32000, "category": "Main Course"},
    17: {"name": "Chicken Cordon Bleu", "stock": 32, "price": 38000, "category": "Main Course"},
    18: {"name": "Meat Lover Pizza", "stock": 25, "price": 55000, "category": "Main Course"},
    19: {"name": "Super Supreme Pizza", "stock": 25, "price": 55000, "category": "Main Course"},
    20: {"name": "Fish N Chip", "stock": 25, "price": 35000, "category": "Main Course"},
    # Snacks_Salty
    21: {"name": "Mix Platter", "stock": 42, "price": 28000, "category": "Salty Snack"},
    22: {"name": "Chicken Wingz", "stock": 38, "price": 22000, "category": "Salty Snack"},
    23: {"name": "French Fries", "stock": 42, "price": 18000, "category": "Salty Snack"},
    24: {"name": "Potato Wedges", "stock": 44, "price": 18000, "category": "Salty Snack"},
    25: {"name": "Pok Pok Chicken", "stock": 40, "price": 24000, "category": "Salty Snack"},
    # Snacks_Sweet
    26: {"name": "Deep Fried Oreo", "stock": 60, "price": 18000, "category": "Sweet Snack"},
    27: {"name": "Ice Cream Pancake", "stock": 26, "price": 24000, "category": "Sweet Snack"},
    28: {"name": "Chocolate Waffle", "stock": 35, "price": 24000, "category": "Sweet Snack"},
    29: {"name": "Cromboloni", "stock": 40, "price": 26000, "category": "Sweet Snack"},
    30: {"name": "Almond Croissant", "stock": 42, "price": 24000, "category": "Sweet Snack"},
}

#========================================================================================================================
#========================================================================================================================

# Declare global order lists and total bills
drink_orders = []
food_orders = []
drink_bill = 0
food_bill = 0

# Section Drinks Function
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


# Function to add a drinks to the menu list
def add_drinks():
    name = input("Enter the name of the drinks: ")
    stock = int(input(f"Enter the stock for {name}: "))
    price = int(input(f"Enter the price for {name}: "))
    category = input(f"Enter the category for {name}: ")
    
    # Check if drinks already exists
    for drinks in drinks_menu.values():
        if drinks["name"].lower() == name.lower():
            print(f"{name} already exists in the menu list.")
            return
    # Find the next available key
    new_key = max(drinks_menu.keys()) + 1 
    # Add the drinks to the menu list
    drinks_menu[new_key] = {"name": name, "stock": stock, "price": price, "category": category}
    print(f"\n{name} has been added successfully.")

# Function to remove a drinks from the menu list based on its name
def remove_drinks():
    name = input("Enter the name of the drinks to remove: ")
    
    # Find the key corresponding to the drinks name
    for key, drinks in drinks_menu.items():
        if drinks["name"].lower() == name.lower():
            del drinks_menu[key]
            print(f"\n{name} has been removed successfully.")
            return
    print(f"{name} was not found in the menu list.")

# Function to buy drinks 
def buy_drinks():
    
    global drink_orders, drink_bill
    global food_orders, food_bill

    print("\n Choose your drink...")
    display_drinks() # To show the drinks menu list

    while True:
        name = input("Enter the name of the drink you want to buy: ")
        quantity = int(input(f"How manny {name}(s) would you like to buy? "))

        # Find the drink in the drinks_menu
        for key, drinks in drinks_menu.items():
            if drinks["name"].lower() == name.lower():
                if drinks["stock"] >= quantity:
                    total_price = quantity * drinks["price"]
                    drinks["stock"] -= quantity
                    drink_bill += total_price
                    drink_orders.append((name, quantity, drinks["price"], total_price))
                    print(f"\nAdded {quantity} {name}(s) to your order.")
                else:
                    print(f"\nSorry, only {drinks["stock"]} {name}(s) are available.")
                break
        else:
            print(f"{name} was not found in the drinks menu")
        
         # Ask if the customer wants to order something else
        more_order = input("Do you want to order something else?: (yes/no)").lower()
        if more_order == "yes":
            what_to_buy = input("What else do you want to buy?: (drink/food)").lower()
            if what_to_buy == "drink":
                continue # Continue to buy more drinks
            elif what_to_buy == "food":
                buy_foods() # Switch to the food-buying function
                return # Exit the drink-buying function after switching to foods
        elif more_order == "no":
            break

    # Print the Bill receipt after all orders are placed
    total_orders = drink_orders + food_orders
    total_bill = drink_bill + food_bill

    if total_orders:
        print("\n" + "=" * 55)
        print("Bill Receipt".center(55))
        print("=" * 55)
        print(f"{'Item':<20}{'Qty':<7}{'Price':<15}{'Total':<12}")
        print("-" * 55)

        for order in total_orders:
            item, qty, price, total = order
            print(f"{item:<20}{qty:<7}Rp{price:<13,.2f}Rp{total:<10,.2f}")
        
        print("=" * 55)
        print(f"{'Total Bill':<42}Rp{total_bill:,.2f}")
        print("=" * 55)
        print("Thanks for ordering at Norway's Cafe!\n".center(55))
        print("Wifi: NorwaysCafe".center(55))
        print("Pass: orderfirst".center(55))
        print("=" * 55)
        
        # Clear the orders and reset the bills
        drink_orders = []
        food_orders = []
        drink_bill = 0
        food_bill = 0
        
    else:
        print("No orders were placed.")

# Function to update drink values based on drink name
def update_drinks():
    
    print("\nUpdating drinks menu...")
    display_drinks()

    while True:
        # Display the current menu
        display_drinks()
        
        # Ask for the name of the drink which we want to update
        drink_name = input("Enter the name of the drink you want to update (or type 'cancel' to exit): ").strip()
        if drink_name.lower() == 'cancel':
            print("Update cancelled.")
            break
        
        # Find the drink by name
        found = False # We have not the drink name yet
        for key, drink in drinks_menu.items():
            if drink['name'].lower() == drink_name.lower():
                found = True # We have found the drink name
                print(f"Current details for {drink['name']}: Stock = {drink['stock']}, Price = Rp{drink['price']:.2f}")
                
                # Ask which attribute we want to update
                update_choice = input("Do you want to update stock, price, or both? ").lower()
                
                if update_choice in ['stock', 'both']:
                    new_stock = int(input(f"Enter the new stock quantity for {drink['name']}: "))
                    drinks_menu[key]['stock'] = new_stock
                
                if update_choice in ['price', 'both']:
                    new_price = int(input(f"Enter the new price for {drink['name']} (in whole number): "))
                    drinks_menu[key]['price'] = new_price

                print(f"\n{drink['name']} has been updated.")
                break
        
        if not found:
            print(f"No drink found with the name '{drink_name}'. Please try again.")

#========================================================================================================================
#========================================================================================================================

# Section Foods Function
# Function to display the list of foods menu
def display_foods(category_filter=None):
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
    print(f"{'ID':<{id_width}}{'Food':<{name_width}}{'Stock':<{stock_width}}{'Price':<{price_width}}")
    print("-" * total_width)

    # Print each food item, applying the category filter if specified
    for foods_id, foods_info in foods_menu.items():
        if category_filter is None or foods_info['category'] == category_filter:
            name = foods_info['name']
            stock = foods_info['stock']
            price = foods_info['price']
            print(f"{foods_id:<{id_width}}{name:<{name_width}}{stock:<{stock_width}}{price:>{price_width},.2f}")

# Function to filter the menu
def display_foods_filter():
    display_foods()  # Display all foods initially

    # Ask the customer if they want to filter the menu
    while True:
        filter_choice = input("\nWould you like to filter the menu by category? (yes/no): ").lower()
        if filter_choice == "yes":
            print("Categories available:")
            print("1. Main Course")
            print("2. Salty Snack")
            print("3. Sweet Snack")
            
            category_choice = input("Please choose a category (main course/salty snack/sweet snack): ").strip().lower()

            if category_choice == "main course":
                display_foods("Main Course")
                print("\nDisplaying Main Course Menu...")
            elif category_choice == "salty snack":
                display_foods("Salty Snack")
                print("\nDisplaying Salty Snack Menu...")
            elif category_choice == "sweet snack":
                display_foods("Sweet Snack")
                print("\nDisplaying Sweet Snack Menu...")
            else:
                print("\nInvalid choice. Please try again.")
            break
        elif filter_choice == "no":
            print("\nDisplaying full menu...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Function to add a foods to the menu list
def add_foods():
    name = input("Enter the name of the foods: ")
    stock = int(input(f"Enter the stock for {name}: "))
    price = int(input(f"Enter the price for {name}: "))
    category = input(f"Enter the category for {name}: ")
    
    # Check if foods already exists
    for foods in foods_menu.values():
        if foods["name"].lower() == name.lower():
            print(f"{name} already exists in the menu list.")
            return
    # Find the next available key
    new_key = max(foods_menu.keys()) + 1 if foods_menu else 1
    # Add the foods to the menu list
    foods_menu[new_key] = {"name": name, "stock": stock, "price": price, "category": category}
    print(f"\n{name} has been added successfully.")

# Function to remove a foods from the menu list based on its name
def remove_foods():
    name = input("Enter the name of the foods to remove: ")
    
    # Find the key corresponding to the foods name
    for key, foods in foods_menu.items():
        if foods["name"].lower() == name.lower():
            del foods_menu[key]
            print(f"\n{name} has been removed successfully.")
            return
    print(f"{name} was not found in the menu list.")

# Function to buy foods 
def buy_foods():
    
    global drink_orders, drink_bill
    global food_orders, food_bill
    
    print("\n Choose your food...")
    display_foods() # To show the foods menu list

    total_orders = [] # To store each order (name, quantity, and price)
    total_bill  = 0 # To accumulate the total price of all orders

    while True:
        name = input("Enter the name of the food you want to buy: ")
        quantity = int(input(f"How manny {name}(s) would you like to buy? "))

        # Find the food in the foods_menu
        for key, foods in foods_menu.items():
            if foods["name"].lower() == name.lower():
                if foods["stock"] >= quantity:
                    total_price = quantity * foods["price"]
                    foods["stock"] -= quantity
                    food_bill += total_price
                    food_orders.append((name, quantity, foods["price"], total_price))
                    print(f"\nAdded {quantity} {name}(s) to your order.")
                else:
                    print(f"\nSorry, only {foods["stock"]} {name}(s) are available.")
                break
        else:
            print(f"{name} was not found in the foods menu")
        
         # Ask if the customer wants to order something else
        more_order = input("Do you want to order something else?: (yes/no)").lower()
        if more_order == "yes":
            what_to_buy = input("What else do you want to buy?: (drink/food)").lower()
            if what_to_buy == "food":
                continue # Continue to buy more foods
            elif what_to_buy == "drink":
                buy_drinks() # Switch to the drink-buying function
                return # Exit the food-buying function after swithcing to drinks
        elif more_order == "no":
            break




    # Print the Bill receipt after all orders are placed
    total_orders = drink_orders + food_orders
    total_bill  = drink_bill + food_bill

    if total_orders:
        print("\n" + "=" * 55)
        print("Bill Receipt".center(55))
        print("=" * 55)
        print(f"{'Item':<20}{'Qty':<7}{'Price':<15}{'Total':<12}")
        print("-" * 55)

        for order in total_orders:
            item, qty, price, total = order
            print(f"{item:<20}{qty:<7}Rp{price:<13,.2f}Rp{total:<10,.2f}")
        
        print("=" * 55)
        print(f"{'Total Bill':<42}Rp{total_bill:,.2f}")
        print("=" * 55)
        print("Thanks for ordering at Norway's Cafe!\n".center(55))
        print("Wifi: NorwaysCafe".center(55))
        print("Pass: orderfirst".center(55))
        print("=" * 55)
        
        # Clear the orders and reset the bills
        drink_orders = []
        food_orders = []
        drink_bill = 0
        food_bill = 0
        
    else:
        print("No orders were placed.")

# Function to update food values based on food name
def update_foods():
    
    print("\nUpdating foods menu...")
    display_foods()
    
    while True:
        # Display the current menu
        display_foods()
        
        # Ask for the name of the food which we want to update
        food_name = input("Enter the name of the food you want to update (or type 'cancel' to exit): ").strip()
        if food_name.lower() == 'cancel':
            print("Update cancelled.")
            break
        
        # Find the food by name
        found = False # We have not the food name yet
        for key, food in foods_menu.items():
            if food['name'].lower() == food_name.lower():
                found = True # We have found the food name
                print(f"Current details for {food['name']}: Stock = {food['stock']}, Price = Rp{food['price']:.2f}")
                
                # Ask which attribute we want to update
                update_choice = input("Do you want to update stock, price, or both? ").lower()
                
                if update_choice in ['stock', 'both']:
                    new_stock = int(input(f"Enter the new stock quantity for {food['name']}: "))
                    foods_menu[key]['stock'] = new_stock
                
                if update_choice in ['price', 'both']:
                    new_price = int(input(f"Enter the new price for {food['name']} (in whole number): "))
                    foods_menu[key]['price'] = new_price

                print(f"\n{food['name']} has been updated.")
                break
        
        if not found:
            print(f"No food found with the name '{food_name}'. Please try again.")

#========================================================================================================================
#========================================================================================================================

# Section Main program 
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

#========================================================================================================================
#========================================================================================================================

# Section Admin Menu
# Function to Admin System Menu
def admin():
        print("\nEntering the Admin System Menu...")
        print("\nPlease enter the admin password: ")
        password = input("Please enter the admin password: ")

        if password == '12345':
            print("\n Welcome to Admin System Menu")
            print("\n1. Add Item")
            print("2. Remove Item")
            print("3. Update item")
            print("4. Exit")

            choice = input("Enter the menu number you want to run: (add item/remove item/update item)").lower().strip()

            if choice == 'add item':
                item_choice = input("Choose what item do you want to add? (drink/food)").lower().strip()
                if item_choice == 'drink':
                    add_drinks()
                elif item_choice == 'food':
                    add_foods()
                else:
                    print("Invalid choice")
                
            elif choice == 'remove item':
                item_choice = input("Choose what item do you want to remove? (drink/food)").lower().strip()
                if item_choice == 'drink':
                    remove_drinks()
                elif item_choice == 'food':
                    remove_foods()
                else:
                    print("Invalid choice")
                    
            elif choice == 'update item':
                item_choice = input("Choose what item do you want to update? (drink/food)").lower().strip()
                if item_choice == 'drink':
                    update_drinks()
                elif item_choice == 'food':
                    update_foods()
                else:
                    print("\nInvalid choice")
                    
            elif choice == 'exit':
                norways_cafe()
            else:
                print("\nInvalid Menu")
            

        else:
            print("\nInvalid password.")
            print("\nReturning to the Main Menu...")

#========================================================================================================================
#========================================================================================================================

# Run the drinks market program
norways_cafe()
