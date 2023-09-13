#1

try:
    day = int(input("Enter a number of the week (1-7): "))

    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        raise Exception("Please enter a valid day")

except Exception as e:
    print(f"Error: {e}")


#2

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 == num2:
        print("Numbers are equal")
    elif num1 < num2:
        print(num1, num2)
    elif num1 > num2:
        print(num2, num1)
except ValueError as e:
    print(f"Error: {e}")

#3

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = input("Enter operation name (+, -, *, /): ")

    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2

    if result == '+':
        print(result1)
    elif result == '-':
        print(result2)
    elif result == '*':
        print(result3)
    elif result == '/':
        if num2 == 0:
            raise ZeroDivisionError ("ZeroDivisionError occured")
        print(result4)

except (ZeroDivisionError) as e:
    print(f"Error: {e}")






