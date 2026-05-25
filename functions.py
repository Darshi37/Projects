#Defining the addition function
#def addition(a, b):
    #summation = a + b    #function code
    #print(summation)
    #return summation     #return the residual value of the code
#result = addition(5, 3)    #Calling addition function with arguments
#print(result)
#print("All done")

#first mini program calculates the gross pay for working 40 hours and beyond
#If user enters an invalid input, the program quits.

def computepay():
    try:
        hours = float(input("Enter hours: "))
        pay_rate = float(input("Enter pay per hour: "))
    except:
        print("Invalid input")
        quit()
    if hours > 40:
        extra_pay = ((hours - 40) * (pay_rate * 1.5))
        gross_pay = 40 * pay_rate + extra_pay
        return gross_pay
    else:
        gross_pay = hours * pay_rate
        return gross_pay
salary = computepay()
print("Your monthly total payment is:",salary)
