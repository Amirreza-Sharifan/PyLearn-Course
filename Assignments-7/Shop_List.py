PRODUCTS = []

def read_from_database():
    file = open("F:/Python/Exercises/7/database.txt", "r")
    for line in file:
        result = line.strip().split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": int(result[3])}
        PRODUCTS.append(my_dict)   
    file.close
    
def write_to_database():
    file = open("F:/Python/Exercises/7/database.txt", "w")
    for product in PRODUCTS:
        new_code = product["code"]
        new_name = product["name"]
        new_price = product["price"]
        new_count = product["count"]
        file.write(new_code)
        file.write(",")
        file.write(new_name)
        file.write(",")
        file.write(new_price)
        file.write(",")
        file.write(str(new_count))
        file.write("\n")
    file.close

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- Exit")

def add():
    code = input("Enter the New Cod: ")
    name = input("Enter the New Name: ")
    price = input("Enter the New Price: ")
    count = input("Enter the New Count: ")
    new_product = {"code": code, "name": name, "price": price, "count":count}
    PRODUCTS.append(new_product)

def edit():
    user_edit = input("Type Your Product for Editing: ")
    for product in PRODUCTS:
        if product["code"] == user_edit or product["name"] == user_edit:
            remove_list = {"code":product["code"], "name":product["name"], "price":product["price"] , "count":product["count"]}
            PRODUCTS.remove(remove_list)
            new_code = input("Enter the New Cod: ")
            new_name = input("Enter the New Name: ")
            new_price = input("Enter the New Price: ")
            new_count = int(input("Enter the New Count: "))
            new_product_edited = {"code": new_code, "name": new_name, "price": new_price, "count":new_count}
            PRODUCTS.append(new_product_edited)
            print("Your Product was found and it Edited to the List") 
            print("You Can Also Enter Number -5- for Watching the Last List")
            break       
    else:
        print("Your Product is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def remove():
    user_remove = input("Type Your Product for Removing: ")
    for product in PRODUCTS:
        if product["code"] == user_remove or product["name"] == user_remove:
            remove_list = {"code":product["code"], "name":product["name"], "price":product["price"] , "count":product["count"]}
            PRODUCTS.remove(remove_list)
            print("Your Product was found and it deleted from the List") 
            print("You Can Also Enter Number -5- for Watching the Last List")
            break       
    else:
        print("Your Product is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def search():
    user_input = input("Please Type Your Keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"],"\t",product["name"],"\t",product["price"],"\4t",product["count"])
            break
    else:
        print("Your Product is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def show_list():
    print("code\t name\t price")
    for product in PRODUCTS:
        print(product["code"],"\t",product["name"],"\t",product["price"])

def buy():
    user_buy = input("Type Your Product for Buying: ")
    for product in PRODUCTS:
        if product["code"] == user_buy or product["name"] == user_buy:
            print("The Data of Your Product is:")
            print("code\t name\t price\t count")
            print(product["code"],"\t",product["name"],"\t",product["price"],"\t",product["count"])
            user_count = int(input("How Many Do You Want From it: "))
            if user_count <= product["count"]:
                new_count = product["count"] - user_count
                remove_list = {"code":product["code"], "name":product["name"], "price":product["price"] , "count":product["count"]}
                PRODUCTS.remove(remove_list)
                new_product_edit_count = {"code":product["code"], "name":product["name"], "price":product["price"], "count":new_count}
                PRODUCTS.append(new_product_edit_count)
                print("You Have Added", (user_count), (product["name"]), "in to Your Cart")
                break
            else:
                print("The Amount of Your Product is More Than Our Capacity")
            break
    else:
        print("Your Product is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

print("Welcome to the AmirrezA online shop")
print("Loading...")
read_from_database()
print("Data Loaded.")
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        write_to_database()
        exit(0)
    else:
        print("Your Number is NOT CORRECT, Please Enter a Valid Number")