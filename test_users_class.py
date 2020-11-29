# Author: Fiona Nganga and Dirac Murairi
# This file is for testing our class User

# we import all the files we need
from users_class import *
import unittest
from unittest import mock
import pytest
import sys
import io

class TestStudent(unittest.TestCase):
    @mock.patch("users_class.input", create=True)
    def test_init_find_specific_book(self, mocked_input):  # this method tests successful borrowing of books in our
        # library which are in the books dictionary, we test the length of our borrowed books to see if the 2 books
        # we borrow are added there
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["swift"]
        i = student.find_specific_book(books)
        assert i == 0

    @mock.patch("users_class.input", create=True)
    def test_pos_find_specific_book(self, mocked_input): # this method is testing the successful
        # extension of a deadline after borrowing
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["PYTHON"]
        i = student.find_specific_book(books)
        assert i == 1

    @mock.patch("users_class.input", create=True)
    def test_pos_search_for_book(self, mocked_input): # this method is testing the successful
        # extension of a deadline after borrowing
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["PYTHON"]
        i = student.search_for_book(books)
        assert i != 0

    @mock.patch("users_class.input", create=True)
    def test_neg_search_for_book(self, mocked_input): # this method is testing the successful
        # extension of a deadline after borrowing
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["Z"]
        i = student.search_for_book(books)
        assert i == 0

    @mock.patch("users_class.input", create=True)
    def test_pos_search_by_auth(self, mocked_input): # this method is testing the successful
        # extension of a deadline after borrowing
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["DIRAC"]
        i = student.search_by_author(books)
        assert i != 0


if __name__ == "__main__":
    unittest.main()
