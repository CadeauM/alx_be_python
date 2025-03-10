def perform_operation(num1, num2, operation):
    if operation.lower() == 'add':
        return num1 + num2
    elif operation.lower() == 'subtract':
        return num1 - num2
    elif operation.lower() == 'multiply':
        return num1 * num2
    elif operation.lower() == 'divide':
        if num2 == 0:
            return "cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
    
