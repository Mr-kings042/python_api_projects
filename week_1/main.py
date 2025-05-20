# Build a simple calculator that can perform addition, subtraction, multiplication, and division.
# The calculator should take two numbers and an operator as input and return the result.
# The calculator should handle invalid input gracefully and provide appropriate error messages.
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x/y

def calculator():
    print("Welcome to  calculator")
    num1 = float(input("Enter your the First Number: "))
    num2 = float(input("Enter the Second Number: "))
    while True:
       operator = input("Choose an Operator(+, -, *, /): ")
       if operator == "+":
           print({f"{num1} + {num2}": add(num1,num2)})
           break
       elif operator == "-":
           print ({f"{num1} - {num2}": subtract(num1,num2)})
           break
       elif operator == "*":
           print ({f"{num1} * {num2}": multiply(num1,num2)})
           break
       elif operator == "/":
            if num2 == 0:
               print ({f"Error": f"Second number: {num2} is 0. Division by zero is not allowed."})
            else:
              result = divide(num1, num2)
              print ({f"{num1} / {num2}": f"{result:.2f}"})
              break
       else:
            print ({f"Error": f"Invalid operator: {operator}. Please use one of the following: +, -, *, /."})
    print("Thank you for using the calculator!")
    
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if another_calculation == "yes":
        calculator()
    else:
        print("Thank you for using Calculator. Goodbye!")


if __name__ == "__main__":
    calculator()