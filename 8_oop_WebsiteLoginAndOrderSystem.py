class User:
    def __init__(self, email, username, password):
        self.email=email
        self.username=username
        self.password=password
        self.is_logged_in= False

    def login(self,username , password):
        if username == self.username and password == self.password:
            self.is_logged_in= True
            print(f"You are logged in now. 🚀")

        else:
            self.is_logged_in= False
            print("Username or password is not correct. ❌")


    def introduce(self):
        return f"{self.username} - {self.email}"

    def __str__(self):
        return self.introduce()


class Admin(User):
    def __init__(self, email, username, password , level="normal"):
        super().__init__(email, username, password)
        self.level=level

    def add_product(self, product_name , product_price):
        if self.is_logged_in:
            print(f"\nA new product with {product_name} title and ${product_price:.2f} has added. ")
        else:
            print("\nYou must be logged in to add a new product.")


class Client(User):
    def __init__(self, email, username, password, credit):
        super().__init__(email, username, password)
        self.credit=credit

    def introduce(self):
        return f"{self.email} - {self.username} - {self.credit}"


    def pay_shopping_card(self, shopping_card_price):
        if self.is_logged_in:
            if self.credit > shopping_card_price:
                self.credit -= shopping_card_price
                print("\nYour shopping card has been payed. ✅")
            else:
                print("\nYou do not have enough credit.")

        else:
            print("You must be logged in.")


user_1=User("gmail.com", "Mahdi", "password")
user_1.login("Mahdi" , "password")
print(user_1.introduce())


admin_1=Admin("email","ali","password")
admin_1.login("ali","password")
admin_1.add_product("pen",100)

client_1=Client("email","mahdi","password",400)
client_1.login("mahdi","password")
client_1.pay_shopping_card(600)



        