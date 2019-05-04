# Introduction to classes in Python.
#
# Author: Omar Barazanji
# Source: https://www.youtube.com/watch?v=cKPlPJyQrt4
# Python Version: 3.7

# Some behavior that I want to implement -> writes some __ function __
class Polynomial:
    def __init__(self, *coeffs): # constructor
        self.coeffs = coeffs

    def __repr__(self): # repr used for representing object (use in terminal)
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)
