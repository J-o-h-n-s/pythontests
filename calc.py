def Add (x, y):
    return x + y

def Subtract (x, y):
    return x - y

def Multiply (x, y):
    return x * y

def Divide (x, y):
    return x / y

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter your choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4',):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", Add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", Subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", Multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", Divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

#next_calculation = input("Do another? (Y/n):")
#if next_calculation == "no":
#        break

else:
    print("Invalid Input")
