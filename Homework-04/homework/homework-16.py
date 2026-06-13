#task1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Студенти
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying for grade {self.grade}.")


# Вчителя
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def get_salary(self):
        print(f"{self.name} earns ${self.salary} per month.")



student1 = Student("Alice", 16, 10)
teacher1 = Teacher("Mr. Smith", 40, "Math", 3000)

student1.introduce()   # Hello, my name is Alice and I am 16 years old.
student1.study()       # Alice is studying for grade 10.

teacher1.introduce()   # Hello, my name is Mr. Smith and I am 40 years old.
teacher1.teach()       # Mr. Smith is teaching Math.
teacher1.get_salary()  # Mr. Smith earns $3000 per month.

print ("\n")

#task 2

class Mathematician:
    def square_nums(self, nums):
        return [x ** 2 for x in nums]

    def remove_positives(self, nums):
        return [x for x in nums if x <= 0]

    def filter_leaps(self, years):
        leap_years = []
        for year in years:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                leap_years.append(year)
        return leap_years

m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

print ("\n")

#task 3

class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0.0

    def add(self, product, amount):
        store_price = product.price * 1.3
        if product.name in self.products:
            self.products[product.name]["amount"] += amount
        else:
            self.products[product.name] = {"product": product, "amount": amount, "price": store_price}

    def set_discount(self, identifier, percent, identifier_type='name'):
        for info in self.products.values():
            if (identifier_type == 'name' and info["product"].name == identifier) or \
               (identifier_type == 'type' and info["product"].type == identifier):
                info["price"] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in store")
        if self.products[product_name]["amount"] < amount:
            raise ValueError(f"Not enough '{product_name}' in store")
        self.products[product_name]["amount"] -= amount
        self.income += self.products[product_name]["price"] * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(info["product"].name, info["amount"], info["price"]) for info in self.products.values()]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in store")
        info = self.products[product_name]
        return (info["product"].name, info["amount"])

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

store = ProductStore()


print ("\n")

#task 4

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        with open("logs.txt", "a") as file:
            file.write(msg + "\n")


try:
    raise CustomException("This is a custom error message!")
except CustomException as e:
    print(f"Caught an error: {e}")


