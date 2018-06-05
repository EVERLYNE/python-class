class student:
  name = "John Doe"
  def _init_(self,name):
    self.name = name
    
  def get_name(self):
    return self.name
      
  def welcom(self):
    return "welcome {} to Akirachix".format(self.name)
    
Fatma = student("Fatma Moha")
Judith = student("Judith mueni")
#print(fatma.welcome())
print(Judith.welcome())