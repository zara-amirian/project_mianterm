class User:  
    def __init__(self, username, password):  
        self.username = username  
        self.password = password  
    def add_address(self, address):
        self.addresses = []          
        self.addresses.append(address)
class Product:
    def __init__(self, name, price):  
        self.name = name  
        self.price = price  
class ShopCart:  
    def __init__(self):  
        self.items = []  
    def add_product(self, product):  
        self.items.append(product)  
    def remove_product(self, product):  
        self.items.remove(product)  
    check = lambda self: sum(product.price for product in self.items)
class Store:  
    def __init__(self):  
        self.users = []  
        self.products = []   
    def register_user(self):  
        username = input("Please enter your username: ")  
        password = input("Please enter your password: ")   
        if username and password:  
            username_exist = False  
            for user in self.users:  
                if user.username == username:  
                    username_exist = True  
                    break  
            if username_exist:  
                print("This username exists!")  
            else:  
                self.users.append(User(username, password))  
                print("Account created successfully")  
    def login_user(self):  
        username = input("Please enter your username: ")  
        password = input("Please enter your password: ")  
        for user in self.users:  
            if user.username == username and user.password == password:   
                self.current_user = user  
                print("Login was successful")  
                return  
            else:
                print("Username or password is incorrect") 
    def add_product(self):  
        name = input("Name of product: ")  
        price = float(input("Price of product: "))  
        self.products.append(Product(name, price))
        print("Product added successfully")  
    def Show_product(self):
        print("\n محصولات موجود: ")
        flag=1
        for product in self.products:
            print(self.format_product(flag, product))
            flag=+1
    def add_to_shopcart(self):
        self.Show_product()
        selection_prod=int(input("Enter product Number to add the ShopCart: "))
        if 0 <= selection_prod<= len(self.products):
            self.ShopCart.add_product(self.products[selection_prod])
            print("Added to cart")
        else:
            print("invalid selection")
    def check(self):  
        final = self.shop_cart.check()  
        print(f"Final costs of products: {final}")  
        confirm = input("Do you confirm the payment? (yes/no) ")  
        if confirm.lower() == 'yes':  
            print("Payment was successfuly")  
            self.shop_cart.items.clear() 
        else:  
            print("Payment canceled")  
store = Store()   
while True:  
    print("\n1. Register")  
    print("2. Login")  
    print("3. Add Product")  
    print("4. Show Products")  
    print("5. Add to Shop Cart")  
    print("6. Payment")  
    print("7. Exit") 
    choice = input("Enter your choice: ")  
    if choice == '1':  
        store.register_user()  
    elif choice == '2':  
        store.login_user()  
    elif choice == '3':  
        store.add_product()  
    elif choice == '4':  
        store.show_products()  
    elif choice == '5':  
        store.add_to_shopcart()  
    elif choice == '6':  
        store.check()  
    elif choice == '7':  
        print("Exiting the program.")  
        break 
    else:  
        print("Invalid selection1 try again.")