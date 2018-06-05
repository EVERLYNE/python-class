class Taxpayer:
  income = 0
  name = "Jane Doe"
  minimum = 0
  def __init__(self,name, income ,minimum):
    self.income = income
    self.name = name 
    self.minimum = minimum
    self.validateIncome()
    self.validateName()
    self.ValidateMinimum()
    
    
  def validateIncome(self):
    if self.income.isnumeric() == False:
      raise ValueError("The income {} is not numeric".format(self.income))
  def validateName(self):
    if self.name .isnumeric():
      raise ValueError("The name {} is not a string".format(self.name))
  def ValidateMinimum(self):
    if float(self.income) < 100001:
      raise ValueError("Bellow minimum wage")
      
  def calculate_tax(self):
    return float (self.income)* 0.3
    
income = input("what is your income")
name = input ("what is your name")
minimum = input("what is your minimum")
employee = Taxpayer(name, income, minimum)
print(employee.calculate_tax())