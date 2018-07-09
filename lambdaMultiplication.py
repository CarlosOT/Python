FunctionLambda = lambda item : item * 2

UserInput = int(input('Inser a value: '))
Value = FunctionLambda(UserInput)

print(f"{UserInput} multiplied by 2 is {Value}")
