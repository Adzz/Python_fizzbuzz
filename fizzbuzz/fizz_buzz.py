"""
  Docstring: class fizzbuzz
  returns fizz on multiples of three
  returns buzz on multiples of five
  returns fizzbuzz on multiples of 15

"""

class FizzBuzz(object):

    def value(self, value):
        if value % 15 == 0:
            return "Fizzbuzz"
        if value % 5 == 0:
            return "Buzz"
        if value % 3 == 0:
            return "Fizz"
        return value

