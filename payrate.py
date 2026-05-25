hours = input("Enter hours: ")
rate = input("Enter rate: ")
otp_rate = 25
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("There is an error with your input")
    quit()    #if the user input is invalid, exit the program without continuing

if hours <= 40:
    salary = hours * rate
    print("The total amount you get:", salary)
elif hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * otp_rate
    salary = overtime_pay + (40*rate)
    print("The total amount you get:", salary)

print("You have worked hard")
print("Have a good day!")

