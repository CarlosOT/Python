class Calculo():
	def calculo_total(self, preco, qtde, desc):
		return (preco * qtde - desc)

result = Calculo()

print(result.calculo_total(15, 15, 10)) 



#------------------------------------ 

class Calculo():
	def calculo_total(self, qtde, desc):
		return (self.preco * qtde - desc)

result = Calculo()
result.preco = 15
print(result.calculo_total(15, 10))

# pode-se imprimir dessa forma também 
print(Calculo.calculo_total(result, 15, 10))
