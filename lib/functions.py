#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()
        
def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Guido!")

def add(num1, num2):
    return num1 + num2
print(add(45, 59))


def halve(num1):
    return num1 / 2
print(halve(100))
    
