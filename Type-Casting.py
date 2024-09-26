#Assigning diffrent variables 

name = "Zain"
age = 12
is_student = True
weight = 35.0

#printing different variables and their data type


print("Name:", name)
print("data type of name is",type(name))

print("age:",age)
print("data type of age is",type(age))

print("is_student:", is_student)
print("data type of is_student is",type(is_student))

print("weight:", weight)
print("data type of weight is",type(weight))

#type casting to convert the data type of variables

print("\n After type casting")

age = str(age)
print(age)
print("data type of age is", type(age))

weight= int(weight)
print(weight)
print("Data type of weight is:",type(weight))