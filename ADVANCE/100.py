class Parent1:
    def speak(self):
        print("Speaking from Parent1.")

class Parent2:
    def greet(self):
        print("Greetings from Parent2.")

class Child(Parent1, Parent2):
    pass

child = Child()
child.speak()  
child.greet()  
