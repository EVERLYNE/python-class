class Rectangle:
  length = 0
  width = 0
  
  def __init__(self,length,width):
    self.length = length
    self.width = width
    self.validateDimension()
   
    
    def ValidateDimensions(self):
      if self.lengh.isnumeric() and self.width. isnumeric)== False:
        raise ValueError("parameters not numeric")
        
    def validateWidth(self):
      if self.width.isnumeric():
        raise ValueError("The width{} is not numeric".format (self.width)
        
        
    
    
  def area(self):
    return self.length *self.width
    
    
  def perimeter(self):
    return 2*(self.length + self.width)
    
small = Rectangle(2,3)
invalid = Rectangle("fixe",5)
print(invalid.area())
