from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"
