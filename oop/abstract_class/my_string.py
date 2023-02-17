from abc import abstractmethod, ABCMeta


class MyString(metaclass=ABCMeta):
    def __init__(self, text):
        self.__text = text

    def __str__(self):
        return self.__text

    @abstractmethod
    def __add__(self, other):
        return MyString(self.__text + '-' + other.__text)
