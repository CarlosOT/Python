def tabuada(x):
    for i in range(1,11):
        s = str(x) + ' x ' + str(i) + ' = ' + str(x * i) + '\r\n'
        f.write(s)


f = open('tentativa.txt','+a')
for j in range(1,101):
    tabuada(j)
    


f.close()
