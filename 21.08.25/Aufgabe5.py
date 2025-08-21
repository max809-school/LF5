num1 = 33
num2 = 8
operators = ["+", "-", "*", "/", "%", "**", "//"]

for operator in operators:
    print(f"{num1} {operator} {num2} = {eval(f'{num1} {operator} {num2}')}")

