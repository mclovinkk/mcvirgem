#solicitar ao usuario que digite um numero
numero = float (input("Digite um numero: "))
#verificar se o numero é positivo, negativo ou zero
if numero > 0:
    print("o numero é positivo.")
elif numero < 0:
    print("o numero é negativo.")
else:
    print("o numero é zero.")