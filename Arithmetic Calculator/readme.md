# Python Calculator

## Overview

This is a simple command-line calculator implemented in Python. It allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division. The results are rounded to three decimal places using the `round()` function for better readability.

## Features

- Supports four basic arithmetic operations:
    - Addition (`+`)
    - Subtraction (`-`)
    - Multiplication (`*`)
    - Division (`/`)
- Input validation for the operator
- Utilizes the `round()` function to round results to three decimal places

## Understanding the Code

The code consists of the following key components:

1. **User Input**:
    
    - The program prompts the user to enter an operator and two numbers.
    
    
```python
	operator = input("Enter an Operator ( + - * / )")
	num1 = int(input("Enter the first Number"))
	num2 = int(input("Enter the second number"))
  ```
  
    
2. **Conditional Logic**:
    
    - The program uses `if`, `elif`, and `else` statements to determine which operation to perform based on the operator entered by the user.
        
```python
	if operator == '+':
	    result = num1 + num2
	elif operator == '-':
	    result = num1 - num2
	elif operator == '*':
	    result = num1 * num2
	elif operator == '/':
	    result = num1 / num2
	else:
    print(f"{operator} is not a valid operator")
```

    
3. **Rounding Results**:
    
    - The `round()` function is used to round the result to three decimal places before displaying it.
    
    python
    
    Copy code
    
```python
    print(round(result, 3))`
```
    
4. **Error Handling**:
    
    - If the user enters an invalid operator, the program will display an appropriate message.

## The `round()` Function

The `round()` function is an important part of this calculator, as it ensures the output is user-friendly by limiting the number of decimal places shown. Here’s how it's used:

python

Copy code

```python
print(round(result, 3))
```

This rounds the `result` to three decimal places, which is particularly useful when dealing with division or other operations that may yield long decimal values.