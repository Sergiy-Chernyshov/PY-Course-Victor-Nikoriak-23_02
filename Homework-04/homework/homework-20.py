# Task1

import unittest


def is_even(number):
    return number % 2 == 0


class TestIsEven(unittest.TestCase):

    def test_even_numbers(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(0))

    def test_odd_numbers(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(99))

    def test_negative_numbers(self):
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(-3))


if __name__ == "__main__":
    unittest.main()

print ("\n")

# Task2

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def get_contact(self, name):
        return self.contacts.get(name)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            return True
        return False

        def test_delete_contact(self):
            result = self.phonebook.delete_contact("Ivan")
            self.assertTrue(result)
            self.assertIsNone(self.phonebook.get_contact("Ivan"))

        def test_delete_non_existing_contact(self):
            result = self.phonebook.delete_contact("Petro")
            self.assertFalse(result)

        def test_update_contact(self):
            result = self.phonebook.update_contact("Ivan", "99999")
            self.assertTrue(result)
            self.assertEqual(self.phonebook.get_contact("Ivan"), "99999")

        def test_update_non_existing_contact(self):
            result = self.phonebook.update_contact("Petro", "11111")
            self.assertFalse(result)

    if __name__ == "__main__":
        unittest.main()