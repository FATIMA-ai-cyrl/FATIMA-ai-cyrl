def greet(name):
    print (f"manal {name}")
greet("bashiru")

def division(a,b):
    return a / b
result = division(30, 5)
print(result)


def arithemetic_operation(a,b):
    return a + b, a - b, a * b, a // b
add, subtract, multiply, divide = arithemetic_operation(30, 5)
print(f"add: {add}, subtract: {subtract}, multiply: {multiply}, divide: {divide}")