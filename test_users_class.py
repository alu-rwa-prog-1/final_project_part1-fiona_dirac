# Author: Fiona Nganga and Dirac Murairi
# This file is for testing our class User

# we import all the files we need
from users_class import *
import unittest
from unittest import mock

class TestSolution(unittest.TestCase):
    @mock.patch("user.input", create=True)
    def negative_test_find_specific_book(self, mocked_input):
        user1 = User("DIRAC", "d.murairi@alustudent.com", 1)
        mocked_input.side_effect = ["SWIFT"]
        i = user1.find_specific_book(books)
        self.assertEqual(i, 0)





if __name__ == "__main__":
    unittest.main()
