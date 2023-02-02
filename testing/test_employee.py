import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Testing employee"""

    def setUp(self):
        self.denis = Employee('Denis', 'Rr', 12200)

    def test_give_default_raise(self):
        self.denis.give_raise()
        self.assertEqual(self.denis.annual_salary, 17200)


if __name__ == '__main__':
    unittest.main()
