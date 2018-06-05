class Student:
  def __init__(self,name,email):
    self.name = name
    self.email =email
    self.validateName()
    self.validateEmail()
    
    
  def validateEmail(self):
    pass
  def validateName(self):
     if type (self.names)is not str:
     raise ValueError("{} is not a valid name".format(self.email))   

jane = Student("Jane","Jane")
print(jane.email)
    