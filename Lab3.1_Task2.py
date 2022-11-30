class Calendar:

    def __init__(self, day: int, month: int, year: int):
        self.year = year
        self.month = month
        self.__day_by_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        self.day = day

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong year type")
        if not value >= 0:
            raise ValueError("Wrong year value")
        self.__year = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong month type")
        if not 1 <= value <= 12:
            raise ValueError("Wrong month value")
        self.__month = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong day type")
        if not value <= self.__day_by_month[self.month]:
            raise ValueError("Wrong day value")
        self.__day = value
        
    def __str__(self):
        if self.day < 10:
            day = "0" + str(self.day)
        else:
            day = str(self.day)
        if self.month < 10:
            month = "0" + str(self.month)
        else:
            month = str(self.month)
        return f"{day}.{month}.{self.year}"

    def add_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

    def sub_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("Can add only int to Calendar type")
        if not other > 0:
            raise ValueError("Can add only positive int to Calendar")
        day = self.day + other
        while not day <= self.__day_by_month[self.month]:
            day -= self.__day_by_month[self.month]
            self.add_month()
        self.day = day
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            raise TypeError("Can subtract only int to Calendar type")
        if not other > 0:
            raise ValueError("Can subtract only positive int to Calendar")
        day = self.day - other
        while not day > 0:
            self.sub_month()
            day += self.__day_by_month[self.month]
        self.day = day
        return self

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Can only compare 2 Calendar type instances")
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False

    def __ne__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Can only compare 2 Calendar type instances")
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return False
        else:
            return True

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Can only compare 2 Calendar type instances")
        if not self.year == other.year:
            return self.year > other.year
        else:
            if not self.month == other.month:
                return self.month > other.month
            else:
                return self.day > other.day

    def __ge__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Can only compare 2 Calendar type instances")
        if not self.year == other.year:
            return self.year > other.year
        else:
            if not self.month == other.month:
                return self.month > other.month
            else:
                return self.day >= other.day

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Can only compare 2 Calendar type instances")
        if not self.year == other.year:
            return self.year < other.year
        else:
            if not self.month == other.month:
                return self.month < other.month
            else:
                return self.day < other.day

    def __le__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Can only compare 2 Calendar type instances")
        if not self.year == other.year:
            return self.year < other.year
        else:
            if not self.month == other.month:
                return self.month < other.month
            else:
                return self.day <= other.day


date1 = Calendar(30, 11, 2022)
date1 += 1
date2 = Calendar(1, 12, 2022)
date3 = Calendar(2, 12, 2022)
print(f"30.11.2022 + 1 = {date1}")
print(f"01.12.2022 == 01.12.2022: {date1 == date2}")
print(f"01.12.2022 > 02.12.2022: {date1 > date3}")
print(f"01.12.2022 >= 01.12.2022: {date1 >= date2}")
date2 += 363
print(f"01.12.2022 + 363 = {date2}")
date3 -= 364
print(f"02.12.2022 - 364 = {date3}")
