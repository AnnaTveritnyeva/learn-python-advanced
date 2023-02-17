class Rectangle:
    __counter = 0

    def __init__(self, width, height):
        Rectangle.__counter += 1
        self.__width = width
        self.__height = height

    def set_size(self, new_width, new_height):
        if new_width > 0:
            self.__width = new_width
        if new_height > 0:
            self.__height = new_height

    def show(self):
        print(self)

    def __str__(self):
        return f"{self.__class__.__name__} width: {self.__width} height: {self.__height}"

    @staticmethod
    def get_counter():
        return Rectangle.__counter
