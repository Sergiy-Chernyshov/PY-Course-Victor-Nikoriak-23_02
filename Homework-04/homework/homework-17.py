#Task1

class Animal:
    def talk(self):
        raise NotImplementedError("реалізація метода")


class Dog(Animal):
    def talk(self):
        print("гав гав")


class Cat(Animal):
    def talk(self):
        print("мяу")

def make_talk(animal: Animal):
    animal.talk()

dog = Dog()
cat = Cat()

make_talk(dog)
make_talk(cat)

print ("\n")

# task2

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}')"

    def __str__(self):
        return f"{self.name} ({self.country})"


class Book:
    total_books_count = 0

    def __init__(self, name, year, author):
        if not isinstance(author, Author):
            raise ValueError("Аргумент 'author' має бути екземпляром класу Author")

        self.name = name
        self.year = year
        self.author = author

        self.author.books.append(self)

        Book.total_books_count += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year})"

    def __str__(self):
        return f"«{self.name}», {self.year} рік (автор: {self.author.name})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        new_book_obj = Book(name, year, author)

        self.books.append(new_book_obj)

        if author not in self.authors:
            self.authors.append(author)

        return new_book_obj

    def group_by_author(self, author: Author):
        results = []
        for book in self.books:
            if book.author == author:
                results.append(book)
        return results

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}')"

    def __str__(self):
        return f"Бібліотека: {self.name} (Книг: {len(self.books)})"


shevchenko = Author("Тарас Шевченко", "Україна", "1814-03-09")

my_lib = Library("Національна бібліотека")

b1 = my_lib.new_book("Кобзар", 1840, shevchenko)
b2 = my_lib.new_book("Гайдамаки", 1841, shevchenko)

print(f"Всього книг створено в системі: {Book.total_books_count}")
print(f"Книги в бібліотеці: {my_lib.books}")
print(f"Книги Шевченка в автора: {shevchenko.books}")

books_1840 = my_lib.group_by_year(1840)
print(f"Книги 1840 року: {books_1840}")

print ("\n")

#task 3

import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменник не може бути рівним нулю.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        common = math.gcd(numerator, denominator)
        self.num = numerator // common
        self.den = denominator // common

    def __add__(self, other):
        # Формула: a/b + c/d = (ad + bc) / bd
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        # Формула: a/b - c/d = (ad - bc) / bd
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        # Формула: a/b * c/d = (ac) / (bd)
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        # Формула: a/b / c/d = (ad) / (bc)
        if other.num == 0:
            raise ZeroDivisionError("Не можна ділити на дріб з чисельником 0.")
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):

        return self.num == other.num and self.den == other.den

    def __lt__(self, other):

        return self.num * other.den < other.num * self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    result_add = x + y
    print(f"{x} + {y} = {result_add}")
    print(f"Перевірка (x + y == 3/4): {result_add == Fraction(3, 4)}")

    print(f"{x} * {y} = {x * y}")

    print(f"{x} - {y} = {x - y}")

    print(f"{x} / {y} = {x / y}")