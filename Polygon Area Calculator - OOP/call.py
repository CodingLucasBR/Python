from rectangle import Rectangle
from square import Square

# Creating an instance of class "Rectangle" and testing the class' methods
rt = Rectangle(10, 5)
print(rt.get_area())
rt.set_height(3)
rt.set_width(20)
print(rt.get_area())
print(rt.get_perimeter())
print(rt.get_diagonal())
print(rt)
print(rt.get_picture())

# Creating an instance of class "Square" and calling the class' methods
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_area())
print(sq.get_perimeter())
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

# Calling the method with two instances
print(rt.get_amount_inside(sq))
