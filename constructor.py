class student:
  name = "John Doe"
  Weekday = True
  
  
  def _init_(self,name,Weekday):
    self.name = name
    self.Weekday
    
  def get_name(self):
    return self.name
      
  def welcom(self):
    return "welcome {} to Akirachix".format(self.name)
    
Fatma = student("Fatma Moha", True)
Judith = student(name "Judith mueni "weekday=False)
print("Fatma:",Fatma.morning())
print("Judith:",Judith.morning())