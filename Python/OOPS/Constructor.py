"""
A constructor is a special method in Python that gets called automatically when an object is created.

Key Points About Constructors:
✔ The constructor method is always named __init__.
✔ It is used to initialize instance variables.
✔ It runs only once per object when the object is created.
✔ If no constructor is defined, Python provides a default constructor.
✔ The constructor must have at least one parameter (self).
✔ The self parameter is a reference to the current instance of the class.
✔in java ans c++ in that class name same as contrctor name.

Self:
-----
self is a reference variable that represents the current instance of the class. 
It is used to access the instance variables and instance methods of that specific object.

Why is self Important?
✔ Identifies the object: Each time an object is created, self allows methods to work with that specific instance.
✔ Accesses instance variables and methods: Without self, Python cannot differentiate between local variables and instance variables.
✔ First parameter in instance methods: Python automatically passes the object reference (self) when calling an instance method.

********an instance variable is the same as a non-static variable. It is a variable that is bound to the object itself*******
"""

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Hello My Name is:", self.name)
        print("My Rollno is:", self.rollno)
        print("My Marks are:", self.marks)


s = Student("John", 101, 90)
s.talk()