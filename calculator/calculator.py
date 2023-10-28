from replit import clear
import art
logo = art.logo

def calculator():
    print(logo)
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1* num2
    def divide(num1, num2):
        if num2 ==float (0):
            print("Divisor can't be 0")
            
        else:
            return num1 / num2
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    number1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    boolean_flag = True
    while boolean_flag:
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))

        calculation_function = operations[operation]
        result = calculation_function(number1, number2)
        print(f"{number1} {operation} {number2} = {result}")
        play_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if play_continue == "y":
            number1 = result
        else:
            boolean_flag = False
            clear
            calculator()
calculator()


    