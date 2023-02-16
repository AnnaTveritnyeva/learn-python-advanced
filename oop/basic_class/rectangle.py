class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_size(self, new_width, new_height):
        if new_width > 0:
            self.__width = new_width
        if new_height > 0:
            self.__height = new_height

    def print(self):
        for h in range(self.__height):
            print(' * ' * self.__width)
