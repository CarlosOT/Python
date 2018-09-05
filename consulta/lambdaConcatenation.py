def concatenation(lastName): return lambda name : name + lastName

lastName = concatenation(' Teixeira')
FullName = lastName('Carlos')

print(FullName)


----------


def fullName():
	name = lambda name, lastName : name + " " + lastName
	return name

myName = fullName()

print(myName('Carlos','Teixeira'))


