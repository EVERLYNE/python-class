def welcome_student(name):
  welcome_str = "Hi {} welcome to akirachix"
  return  welcome_str.format(name)
  
name = input("enter student name:")
print(welcome_student (name))
print(welcome_student ("joice"))
print(welcome_student ("mary"))
print(welcome_student ("lea"))
print(welcome_student ("maureen"))
