from oop.inheritance.rectangle import Rectangle


class RoundedRectangle(Rectangle):
    def __init__(self, width, height, angle):
        super().__init__(width, height)
        self.__angle = angle

    def set_angle(self, angle):
        self.__angle = angle

    def __str__(self):
        return super().__str__() + f" angle: {self.__angle} "

    def show(self):
        super().show()
