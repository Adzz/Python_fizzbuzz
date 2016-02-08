import unittest
from fizzbuzz.fizz_buzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self):
        pass

    def test_FizzBuzz_returns_Fizz_on_multiples_of_three(self):
        assert self.fizzbuzz.value(3) == "Fizz"

    def test_FizzBuzz_returns_the_number_on_numbers_that_arent_multiples_of_three_or_five_or_fifteen(self):
        assert self.fizzbuzz.value(1) == 1
        assert self.fizzbuzz.value(7) == 7
        assert self.fizzbuzz.value(17) == 17

    def test_FizzBuzz_returns_Buzz_on_multiples_of_five(self):
        assert self.fizzbuzz.value(5) == "Buzz"

    def test_FizzBuzz_returns_Fizzbuzz_on_multiples_of_fifteen(self):
        assert self.fizzbuzz.value(15) == "Fizzbuzz"


