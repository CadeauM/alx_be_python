def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'cannot divide by zero'
        return num1 / num2
    else:
        return 'invalid operation'
    
    