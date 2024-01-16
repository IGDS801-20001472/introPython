num1 = 20
num2 = 4

print(" la suma es: ", (num1+num2))
print(" la resta es: ", (num1-num2))
print(" la multiplicacion es: ", (num1*num2))
print(" la division es: ", (num1/num2))
print(" la division exacta es: ", (num1//num2))
print(" la potencia es: ", (num1+num2))



#concateniacion en python

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)


print("El saludo es: %s %s" %(texto1, texto2))

saludoFinal = "Saludo2 : {} {}".format(texto1,texto2)

saludoFinal2 = "Saludo3 : {y} {x}".format(x=texto1,y=texto2)
print(saludoFinal2)
