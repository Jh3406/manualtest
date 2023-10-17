import calculator

selection = int( input("\nSelect your calculator operation: \
                       \n1.Addition\
                       \n2.Subtraction\
                       \n3.Multiplication\
                       \n4.Division\n"))

num1 = calculator.get_inp("First value: ")
num2 = calculator.get_inp("Second value: ")

#if selection == 1:
match selection:
    case 1:
        result = calculator.add(num1, num2)
    case 2:
        result = calculator.subtract(num1, num2)
    case 3:
        result = calculator.multiply(num1, num2)
    case 4:
        result = calculator.divide(num1, num2)

print(f"\nThe result is : {result}")


#Add code here