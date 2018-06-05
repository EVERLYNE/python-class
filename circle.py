
class circle:
  radius = 0
  diameter= 0
  
  def __init__(self,radius,diameter):
    self.radius = radius
    self.diameter = diameter
    
  def area(self):
    return 3.142*(self.radius *self.radius)
    
    
  def perimeter(self):
    return (2*3.142* self.radius)
    
small = circle(4,5)
large = circle(10,12)
print("radius and diameter of smaller {} and {}".format(small.radius,small.diameter))
print("smaller area",small.area())
print("larger area",large.area())

small = circle(8,10)
large = circle(14,7)
print("radius and diameter of smaller {} and {}".format(small.radius,small.diameter))
print("smaller perimeter",small.perimeter())
print("larger perimeter",small.perimeter())
