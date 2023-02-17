class MyString:
    def __init__(self, text):
        self.__text = text

    def __str__(self):
        return self.__text

    def __add__(self, other):
        return MyString(self.__text + "-" + other.__text)
