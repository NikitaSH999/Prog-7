def main():
    '''
    Program name: simple calculator
    It do some calculation
    '''
    #print(main.__doc__)
    while True:
        print('Operations:')
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'quit' to end the program")
        user_input = input('Your enter: ')
        
        if user_input == 'quit':
            print('Goodbye!')
            break
        
        elif user_input == 'add':
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            result = str(num1 + num2)
            print('Result: ' + result)
        
        elif user_input == 'subtract':
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            result = str(num1 - num2)
            print('Result: ' + result)
        
        elif user_input == 'multiply':
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            result = str(num1 * num2)
            print('Result: ' + result)
        
        elif user_input == 'divide':
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
            result = str(num1 / num2)
            print('Result: ' + result)
        
        else:
            print('Unknown input. Try again :)')
            
main()