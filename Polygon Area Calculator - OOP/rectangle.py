# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
from math import floor


class Rectangle:

    def __init__(self, width: int, height: int):
        assert width > 0, f"Width {width} is not greater than zero"
        assert height > 0, f"Height {height} is not greater than zero"

        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return round((self.width ** 2 + self.height ** 2) ** .5, 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for ii in range(1, self.height + 1):
                for jj in range(1, self.width + 1):
                    picture += "* "
                picture += "\n"
        return picture

    def get_amount_inside(self, self2):  # self2 = passed in shape
        area1 = self.get_area()
        area2 = self2.get_area()
        return floor(area1 / area2)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
