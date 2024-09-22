num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

match operation:
    case "+":
        result = num1 + num2
        print('The result is ', result)
    case "-":
        result = num1 - num2
        print('The result is ', result)
    case "*":
        result = num1 * num2
        print('The result is ', result)
    case "/":
        result = num1 / num2
        print('The result is ', result)

        if num2 != 0:
            result = num1 / num2
        else:
            print('Cannot divide by Zero')
    case _:
        print('Invalid operation. Please choose one of (+, -, *, /) ')
