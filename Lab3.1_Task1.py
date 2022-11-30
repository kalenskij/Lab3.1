from math import gcd


class Rational:

    def __init__(self, numerator: int, denominator: int):
        """
        :param numerator: Numerator of the rational number
        :param denominator: Denominator of the rational number
        """
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong numerator type")
        if not value >= 0:
            raise ValueError("Wrong numerator value")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong denominator type")
        if not value > 0:
            raise ValueError("Wrong denominator value")
        self.__denominator = value

    def __str__(self):
        numerator = self.numerator//gcd(self.numerator, self.denominator)
        denominator = self.denominator//gcd(self.numerator, self.denominator)
        return f"{numerator}/{denominator}"

    def __add__(self, other):
        result_numerator = self.numerator*other.denominator + other.numerator*self.denominator
        result_denominator = self.denominator*other.denominator
        result_numerator = result_numerator//gcd(self.numerator, self.denominator)
        result_denominator = result_denominator//gcd(self.numerator, self.denominator)
        return Rational(result_numerator, result_denominator)

    def __sub__(self, other):
        result_numerator = self.numerator*other.denominator - other.numerator*self.denominator
        result_denominator = self.denominator*other.denominator
        result_numerator = result_numerator // gcd(self.numerator, self.denominator)
        result_denominator = result_denominator // gcd(self.numerator, self.denominator)
        return Rational(result_numerator, result_denominator)

    def __mul__(self, other):
        result_numerator = self.numerator*other.numerator
        result_denominator = self.denominator*other.denominator
        result_numerator = result_numerator // gcd(self.numerator, self.denominator)
        result_denominator = result_denominator // gcd(self.numerator, self.denominator)
        return Rational(result_numerator, result_denominator)

    def __truediv__(self, other):
        result_numerator = self.numerator*other.denominator
        result_denominator = self.denominator*other.numerator
        result_numerator = result_numerator // gcd(self.numerator, self.denominator)
        result_denominator = result_denominator // gcd(self.numerator, self.denominator)
        return Rational(result_numerator, result_denominator)

    def __gt__(self, other):
        numerator1 = self.numerator*other.denominator
        numerator2 = other.numerator*self.denominator
        return numerator1 > numerator2

    def __lt__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 < numerator2

    def __eq__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 == numerator2

    def __ge__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 >= numerator2

    def __le__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 <= numerator2

    def __ne__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 != numerator2

    def get_float(self):
        return self.numerator/self.denominator


n1 = Rational(1, 4)
n2 = Rational(1, 2)
print(n1)
print(f"1/4 + 1/2 = {n1+n2}")
print(f"1/4 > 1/2: {n1>n2}")
print(f"1/4 < 1/2: {n1<n2}")
print(f"1/4 + 1/4 == 1/2: {n1+n1 == n2}")
print(f"1/4 + 1/4 >= 1/2: {n1 + n1 >= n2}")
print(f"1/4 > 1: {n1 > 1}")
print(f"1/4 < 1: {n1 < 1}")
