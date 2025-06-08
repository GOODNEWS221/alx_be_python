def perform_operation(num1, num2, operation):
    """
    Performs an arithmetic operation on two numbers.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): Operation ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - float: Result of the operation
    - str: Error message for invalid input or divide by zero
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
    
    