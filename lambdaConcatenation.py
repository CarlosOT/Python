def concatenation(lastName): return lambda name : name + lastName

lastName = concatenation(' Teixeira')
FullName = lastName('Carlos')

print(FullName)