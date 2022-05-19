import math
from point_2d import Point2D

p1 = Point2D(1, 1)
p2 = Point2D(-3, -1)
p3 = Point2D(-3, 2)

d = p1.distance(p2)
d2 = p2.distance(p1)

# print(d)
# print(d2)

d3 = Point2D.distance(p1, p2)

difference = p1 - p3
print(difference)

[1, 2, 3, 4]
