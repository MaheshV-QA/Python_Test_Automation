
"""
static method :
 A  staticmethod  is a method that doesn’t take any implicit first argument (neither  self  nor  cls ).
It behaves like a regular function but belongs to the class’s namespace. 
I typically use  staticmethod  when I need a utility function that logically belongs to the class but doesn’t 
interact with the instance or class itself.

A  classmethod , on the other hand, takes the class itself as the first argument, conventionally named  cls . 
It can access or modify the class state and is used when I want to work with the class rather than its instances.


"""
#  Here’s an example illustrating both: 

class MyClass:
    class_variable = 0

    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        print(f"Class variable is now {cls.class_variable}")

MyClass.static_method()   # Output: This is a static method.
MyClass.class_method()    # Output: Class variable is now 1