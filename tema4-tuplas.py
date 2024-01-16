'''

la tupla es inmutable

'''

tupla = ["uno","dos","tres"]

print(tupla)

tuplaVariosDatos = (12,True,23.5,"El Gato", 1234)
print(tuplaVariosDatos)


tuplasConTuplas(1,2,3,(1,2,3))
print(tuplasConTuplas)

print(tuplasConTuplas[1])
print(tuplasConTuplas[2])
print(tuplasConTuplas[3])


a,b,c = tupla
print(a)
print(b)
print(c)


tuplaNueva = tupla + tuplaVariosDatos

print(tuplaNueva)

