name = input("What is your name?")
print("The name is:",name)

age = input("What is your age?")
print("The age is:",age)
age = int(age)
print(type(age))

salary_hour = int(input("What is your salary per hour?"))
print(type(salary_hour))

value = int(input("What is your lucky number?"))
while value > 0:
    value = value - 1
    print(value,end="")
    if value > 0:
        print(",", end="")
print("\nall numbers are printed sucessfully")
