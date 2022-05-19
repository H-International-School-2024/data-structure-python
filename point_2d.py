import math

class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __sub__(self, p2):
    return self.distance(p2)

  def distance(self, other_point):
    delta_x = self.x - other_point.x
    delta_y = self.y - other_point.y
    return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))

  def distance(p1, p2):
    delta_x = p1.x - p2.x
    delta_y = p1.y - p2.y
    return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))