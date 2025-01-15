class Car:
    def __init__(self, make="Honda", model="Civic", year=2021):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

car1 = Car("BMW", "X5", 2022)
car1.display_info()

car2 = Car()
car2.display_info()
