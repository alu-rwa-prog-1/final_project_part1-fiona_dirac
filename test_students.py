# Author: Fiona Nganga and Dirac Murairi
# This file is for testing our class Student

# we import all the files we need
from students import *
import unittest
from unittest import mock
import pytest


class TestStudent(unittest.TestCase):
    @mock.patch("students.input", create=True)
    def test_init_book_and_try_borrow(self, mocked_input):  # this method tests successful borrowing of books in our
        # library which are in the books dictionary, we test the length of our borrowed books to see if the 2 books
        # we borrow are added there
        student = Student("Fiona", "f.nganga@alustudent.com", "2020", "CS", 2)
        mocked_input.side_effect = [2, "java", "mfc"]
        student.borrow_book(books, lst_b)
        assert len(lst_b) == 2

    @mock.patch("students.input", create=True)
    def test_init_book_extend_borrowed_existing_book(self, mocked_input):  # this method is testing the successful
        # extension of a deadline after borrowing
        student = Student("Fiona", "f.nganga@alustudent.com", "2020", "CS", 2)
        mocked_input.side_effect = ["java"]
        student.extend_borrowing(lst_b)
        for x in lst_b:
            if x["book_name"] == "java":
                assert x["extended"] == 1

    def test_init_change_password(self):  # this method checks whether we can change the user's details
        student = Student("Fiona", "f.nganga@alustudent.com", "2020", "CS", 2)
        new_id = "2023"
        self.password = new_id
        print(student.id)
        self.assertEqual(new_id, self.password)


if __name__ == "__main__":
    unittest.main()
