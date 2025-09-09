def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "\033[31mERROR\033[0m"
    return a / b
def power(a, b):
    return a ** b

print("____eassy calculator____")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. power")
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
operation = int(input("Enter operation choice: "))
print("")

if operation == 1:
    print(f"{a} + {b} = {add(a, b)}")
elif operation == 2:
    print(f"{a} - {b} = {subtract(a, b)}")
elif operation == 3:
    print(f"{a} * {b} = {multiply(a, b)}")
elif operation == 4:
    print(f"{a} / {b} = {divide(a, b)}")
elif operation == 5:
    print(f"{a} ** {b} = {power(a, b)}")
else:
    print("invalid choice")
