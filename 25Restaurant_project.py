list_of_rest = {
    101: "Biryani House",
    102: "Pizza Corner",
    103: "Green Leaf Restaurant"}
res_id = ""
cart = {}
order_history = []
applied_coupon = None
next_order_id = 1001
list_1 = [{"food_id": 1, "food_item": "Chicken Biryani", "price": 180, "type": "Non-Veg"},
          {"food_id": 2, "food_item": "Mutton Biryani", "price": 250, "type": "Non-Veg"},
          {"food_id": 3, "food_item": "Veg Biryani", "price": 140, "type": "Veg"}]
list_2 = [{"food_id": 1, "food_item": "Margherita Pizza", "price": 160, "type": "Veg"},
          {"food_id": 2, "food_item": "Chicken Pizza", "price": 240, "type": "Non-Veg"},
          {"food_id": 3, "food_item": "Paneer Pizza", "price": 210, "type": "Veg"}]


list_3 = [{"food_id": 1, "food_item": "Veg Meals", "price": 120, "type": "Veg"},
          {"food_id": 2, "food_item": "Paneer Fried Rice", "price": 170, "type": "Veg"},
          {"food_id": 3, "food_item": "Mushroom Noodles", "price": 190, "type": "Veg"}]


def view_Restaurants():
    print("\n**********Restaurants**********")
    print("Restaurant_Id | Restaurant_Names")
    print("*******************************")
    print("     101      | Biryani House")
    print("     102      | Pizza Corner")
    print("     103      | Green Leaf Restaurant")

# from view import view_Restaurants 

def Select_Restaurant():
    global res_id
    res_id = input("\nenter your restaurant ID :")
    if res_id == "101":
        print(f"\nyou are selected {list_of_rest[101]}")
    elif res_id == "102":
        print(f"\nyou are selected {list_of_rest[102]}")
    elif res_id == "103":
        print(f"\nyou are selected {list_of_rest[103]}")
    else:
        print("\nRestaurant not found")


def View_Menu():
    if res_id == "":
        print("\nFirst select restaurant to View_Menu")
        return
    elif res_id == "101":
        print("\n***********Biryani House************")
        print("| Food Id | Food Item       | price | Type    |")
        print("|---------------------------------------------|")
        print("| 1.      | Chicken Biryani | ₹180  | Non-Veg |")
        print("| 2.      | Mutton Biryani  | ₹250  | Non-Veg |")
        print("| 3.      | Veg Biryani     | ₹140  | Veg     |")
    elif res_id == "102":
        print("\n************Pizza Corner*************")
        print("| Food Id | Food Item        | price | Type    |")
        print("|----------------------------------------------|")
        print("| 1.      | Margherita Pizza | ₹160  | Veg     |")
        print("| 2.      | Chicken Pizza    | ₹240  | Non-Veg |")
        print("| 3.      | Paneer Pizza     | ₹210  | Veg     |")
    elif res_id == "103":
        print("\n*******Green Leaf Restaurant*******")
        print("| Food Id | Food Item         | price | Type |")
        print("|--------------------------------------------|")
        print("| 1.      | Veg Meals         | ₹120  | Veg  |")
        print("| 2.      | Paneer Fried Rice | ₹170  | Veg  |")
        print("| 3.      | Mushroom Noodles  | ₹190  | Veg  |")


def Search_Food():
    if res_id == "":
        print("\nFirst select restaurant to Search_Food")
    elif res_id == "101":
        search = input("\nEnter a food name to search :").lower()
        list_1 = [["1.", "Chicken Biryani", "₹180", "Non-Veg"], ["2.",
                "Mutton Biryani", "₹250", "Non-Veg"], ["3.", "Veg Biryani", "₹140", "Veg"]]
        isfound = True
        for i in range(len(list_1)):
            if search == list_1[i][1].lower():
                print(list_1[i])
                isfound = False
        if isfound:
            print("Food Not found")
    elif res_id == "102":
        search = input("\nEnter a food name to search :").lower()
        list_2 = [["1.", "Margherita Pizza", "₹160", "Veg"], ["2. ",
            "Chicken Pizza", "₹240", "Non-Veg"], ["3.", "Paneer Pizza", "₹210", "Veg"]]
        isfound = True
        for i in range(len(list_2)):
            if search == list_2[i][1].lower():
                print(list_2[i])
                isfound = False
        if isfound:
            print("Food Not found")
    elif res_id == "103":
        search = input("\nEnter a food name to search :").lower()
        list_3 = [["1.", "Veg Meals", "₹120", "Veg"], ["2.", 
            "Paneer Fried Rice", "₹170", "Veg"], ["3.","Mushroom Noodles", "₹190", "Veg"]]
        isfound = True
        for i in range(len(list_3)):
            if search == list_3[i][1].lower():
                print(list_3[i])
                isfound = False
        if isfound:
            print("Food Not found")


def Filter_Food_by_Price():
    if res_id == "":
        print("\nFirst select restaurant to Filter_Food_by_Price")
    elif res_id == "101":
        price = float(input("\nEnter your maximum price: ₹"))
        print("\nFood items within your budget:")
        filter = True
        for i in list_1:
            if i["price"] <= price:
                print(
                    f'{i["food_id"]}. — {i["food_item"]} — ₹{i["price"]} — {i["type"]}')
                filter = False
        if filter:
            print("No food founded in given price")
    elif res_id == "102":
        price = float(input("\nEnter your maximum price: ₹"))
        print("\nFood items within your budget:")
        filter = True
        for i in list_2:
            if i["price"] <= price:
                print(
                    f'{i["food_id"]}. — {i["food_item"]} — ₹{i["price"]} — {i["type"]}')
                filter = False
        if filter:
            print("No food founded in given price")
    elif res_id == "103":
        price = float(input("\nEnter your maximum price: ₹"))
        print("\nFood items within your budget:")
        filter = True
        for i in list_3:
            if i["price"] <= price:
                print(
                    f'{i["food_id"]}. — {i["food_item"]} — ₹{i["price"]} — {i["type"]}')
                filter = False
        if filter:
            print("No food founded in given price")


def Filter_Veg_or_Non_Veg_Food():
    if res_id == "":
        print("\nFirst select restaurant to Filter_Veg_or_Non_Veg_Food")
    elif res_id == "101":
        enter = input("\nTo Choose Veg or Non-Veg :").lower()
        for i in list_1:
            if enter == i["type"].lower():
                print(f'{i["food_id"]}. — {i["food_item"]}')
            elif enter == i["type"].lower():
                print(f'{i["food_id"]}. — {i["food_item"]}')
    elif res_id == "102":
        enter = input("\nTo Choose Veg or Non Veg :").lower()
        for i in list_2:
            if enter == i["type"].lower():
                print(f'{i["food_id"]}. — {i["food_item"]}')
            elif enter == i["type"].lower():
                print(f'{i["food_id"]}. — {i["food_item"]}')
    elif res_id == "103":
        enter = input("\nTo Choose Veg or Non Veg :").lower()
        for i in list_1:
            if enter == i["type"].lower():
                print(f'{i["food_id"]}. — {i["food_item"]}')
            elif enter == i["type"].lower():
                print(f'{i["food_id"]}. — {i["food_item"]}')


def Add_Food_to_Cart():
    if res_id == "":
        print("\nFirst select restaurant to Add_Food_to_Cart")
    elif res_id == "101":
        enter = int(input("\nEnter your food_id :"))
        filter = True
        for i in list_1:
            if enter == i["food_id"]:
                quantity = int(input("\nEnter food Quantity :"))
                if i["food_item"] not in cart:
                    cart[i["food_item"]] = quantity
                    print("\nDish added to the Cart")
                    filter = False
                else:
                    cart[i["food_item"]] += quantity
                    print("\nDish updated to the Cart")
                    filter = False
        if filter:
            print("Food not found")
    elif res_id == "102":
        enter = int(input("\nEnter your food_id :"))
        filter = True
        for i in list_2:
            if enter == i["food_id"]:
                quantity = int(input("\nEnter food Quantity :"))
                if i["food_item"] not in cart:
                    cart[i["food_item"]] = quantity
                    print("\nDish added to the Cart")
                    filter = False
                else:
                    cart[i["food_item"]] += quantity
                    print("\nDish updated to the Cart")
                    filter = False
        if filter:
            print("Food not found")
    elif res_id == "103":
        enter = int(input("\nEnter your food_id :"))
        filter = True
        for i in list_3:
            if enter == i["food_id"]:
                quantity = int(input("\nEnter food Quantity :"))
                if i["food_item"] not in cart:
                    cart[i["food_item"]] = quantity
                    print("\nDish added to the Cart")
                    filter = False
                else:
                    cart[i["food_item"]] += quantity
                    print("\nDish updated to the Cart")
                    filter = False
        if filter:
            print("Food not found")


def Remove_Food_from_Cart():
    if cart == {}:
        print("\nFirst add dish to cart then remove items!")  
        return      
    enter = input("Enter Dish to remove from cart :").title()
    del cart[enter]
    print(f'{enter} has been removed')


def View_Cart():
    if cart == {}:
        print("\nNo dishes added to the cart!")
    else:
        print("-------Cart-------")
        for i in cart.items():
            print(f' {i[0]} — {i[1]} ')


def Apply_Coupon():
    global applied_coupon
    if not cart:
        print("\nAdd items to the cart before applying a coupon.")
        return

    menus = [list_1, list_2, list_3]
    subtotal = 0
    for i, j in cart.items():
        food = next((item for menu in menus for item in menu
                     if item["food_item"] == i), None)
        if food:
            subtotal += food["price"] * j   

    coupon = input("Enter coupon code (FOOD10 or SAVE50): ").strip().upper()
    if coupon == "FOOD10":
        minimum, discount = 300, subtotal * 0.10
    elif coupon == "SAVE50":
        minimum, discount = 500, 50
    else:
        print("Invalid coupon code")
        return
    if subtotal < minimum:
        print(f"Minimum order for {coupon} is ₹{minimum}.")
        return
    applied_coupon = coupon
    print(f"Coupon {coupon} applied. Discount: ₹{discount:g}")


def Checkout():
    global applied_coupon, next_order_id
    if not cart:
        print("\nYour cart is empty. Add food before checkout.")
        return

    menus = [list_1, list_2, list_3]
    items = []
    subtotal = 0
    for i,j in cart.items():
        food = next((item for menu in menus for item in menu
                     if item["food_item"] == i), None)
        if food:
            subtotal += food["price"] * j
            items.append({"food_item": i, "quantity": j,
                          "price": food["price"]})
    if subtotal < 200:
        print("Minimum order amount is ₹200.")
        return

    discount = 0
    if applied_coupon == "FOOD10" and subtotal >= 500:
        discount = subtotal * 0.10
    elif applied_coupon == "SAVE50" and subtotal >= 300:
        discount = 50
    elif applied_coupon:
        print("Applied coupon no longer meets its minimum order amount.")
        applied_coupon = None
        
    final_amount = subtotal - discount
    order_history.append({"order_id": next_order_id, "items": items,
                          "amount": final_amount})
    print("\nOrder placed successfully!")
    print(f"Order ID: {next_order_id}")
    print(f"Subtotal: ₹{subtotal}")
    print(f"Discount: ₹{discount:g}")
    print(f"Final payable amount: ₹{final_amount:g}")
    next_order_id += 1
    cart.clear()
    applied_coupon = None


def View_Order_History():
    if not order_history:
        print("\nNo orders have been placed yet.")
        return
    print("\n------- Order History -------")
    for order in order_history:
        print(f"\nOrder ID: {order['order_id']}")
        for item in order["items"]:
            print(f"{item['food_item']} — ₹{item['price'] * item['quantity']}")
        print(f"Final amount: ₹{order['amount']:g}")


def main():
    print("========== FOOD DELIVERY APP ==========\n")
    while True:
        print("\n1. View Restaurants")
        print("2. Select Restaurant")
        print("3. View Menu")
        print("4. Search Food")
        print("5. Filter Food by Price")
        print("6. Filter Veg / Non-Veg Food")
        print("7. Add Food to Cart")
        print("8. Remove Food from Cart")
        print("9. View Cart")
        print("10. Apply Coupon")
        print("11. Checkout")
        print("12. View Order History")
        print("13. Exit\n")

        choice = int(input("enter your choice :"))

        if choice == 1:
            view_Restaurants()
        elif choice == 2:
            Select_Restaurant()
        elif choice == 3:
            View_Menu()
        elif choice == 4:
            Search_Food()
        elif choice == 5:
            Filter_Food_by_Price()
        elif choice == 6:
            Filter_Veg_or_Non_Veg_Food()
        elif choice == 7:
            Add_Food_to_Cart()
        elif choice == 8:
            Remove_Food_from_Cart()
        elif choice == 9:
            View_Cart()
        elif choice == 10:
            Apply_Coupon()
        elif choice == 11:
            Checkout()
        elif choice == 12:
            View_Order_History()
        elif choice == 13:
            print("Thank you!")
            break
        else:
            print("Invalid choice")


main()
