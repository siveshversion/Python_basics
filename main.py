#6 Important Python Concepts

#1 Variables

name = 'Ashok'
age = '28'

print(name, age)


#2 Basic Data Types:

number: int = 10
decimal: float =  2.5
text: str = 'Hello World'
active: bool = True

names: list = ['Ashok', 'Sivesh', 'Kumar']
coordinates: tuple = (1.5,2.5)
unique: set = {1,2,3,4,5,4}
data: dict = {'name': 'Ashok', 'age': 28}

print(unique)

#3 Type annotations

name: str = 'Ashok'

#4 Constants
from typing import Final
VERSION: Final[str] = '1.0.1'

print(VERSION)


#5 Functions
def greet(name: str) -> str:
    print(f'Hello {name}')

greet('Ashok')

def hello() -> str:
    return 9

print( hello())

#6 classes, Methods & Dunder Methods
from typing import Self

class Car:
    def __init__(self,brand: str, horsepower: int) -> None:
        self.brand = brand,
        self.horsepower = horsepower

    def drive(self) -> None:
        print(self.brand, self.horsepower)

    def __add__(self, other:Self):
      return f' I\'m driving {self.brand} & without {other.horsepower} of horse power'

volvo: Car = Car('VOLVO', 2344)
print(volvo.brand)
print(volvo.horsepower)

print(volvo.drive())

BMW: Car = Car('BMW', 3423)
print(volvo  +  BMW)





