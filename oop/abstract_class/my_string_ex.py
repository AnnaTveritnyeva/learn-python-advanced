from oop.abstract_class.my_string import MyString


class MyStringEx(MyString):

    def __add__(self, other):
        return MyStringEx(self._MyString__text + '*' + other._MyString__text)
