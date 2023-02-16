class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_size(self, width, height):
        self.__width = width
        self.__height = height

    def print(self):
        for h in range(self.__height):
            print(' * ' * self.__width)
