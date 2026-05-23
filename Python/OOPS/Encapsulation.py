"""
Encapsulation
---------------
• The process of wrapping the data members(Global variables) and member function(methods) into a 
single unit(class) is called as Encapsulation.

• The main purpose of encapsulation is to achieve security of data.

In Python, encapsulation is implemented using access modifiers:

Public (var) → Accessible from anywhere.

Protected (_var) → Should only be accessed within the class and its subclasses.

Private (__var) → Cannot be accessed directly outside the class.

"""

class Login:
    def __init__(self):
        self.__username = None  # Private attribute
        self.__pwd = None       # Private attribute

    # Setter for username
    def set_username(self, username):
        self.__username = username

    # Getter for username with validation
    def get_username(self):
        if self.__username == "John":
            return "Username is correct, Please Enter Password"
        else:
            return "Username is Incorrect"

    # Setter for password
    def set_pwd(self, pwd):
        self.__pwd = pwd

    # Getter for password with validation
    def get_pwd(self):
        if self.__pwd == "John@14141":
            return "Please go ahead"
        else:
            return "Entered password is invalid"


# Creating an instance of Login class
l1 = Login()

# Setting username
l1.set_username("John")
print(l1.get_username())  # ✅ Output: Username is correct, Please Enter Password

# Setting password
l1.set_pwd("Something@143")
print(l1.get_pwd())  # ❌ Output: Entered password is invalid
