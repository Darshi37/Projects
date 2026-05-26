largest = 0
smallest = None

while True:
    number = input("Enter a number: ")
    if number == "done":
        break

    try:
        number = int(number)
        if number > largest:
            largest = number
        if smallest == None:
            smallest = number
        if number < smallest:
            smallest = number
    except:
        print("Invalid input")

print("maximum number is:", largest)
print("minimum number is:", smallest)





