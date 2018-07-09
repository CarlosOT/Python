FunctionLambda = lambda item : item * 2

UserInput = int(input('Inser a value: '))
Value = FunctionLambda(UserInput)

print(f"{UserInput} multiplied by 2 is {Value}")

----------------------------

def multiplicator(n): return lambda item : item * n

value = multiplicator(3)
resultado = value(3)

print(resultado)
