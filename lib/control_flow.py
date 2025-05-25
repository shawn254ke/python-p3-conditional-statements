#!/usr/bin/env python3

def admin_login(username, password):
    
    return "Access granted" if (username == "admin" or username == "ADMIN" )and password == "12345" else "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"
    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    op = operation.strip()
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
