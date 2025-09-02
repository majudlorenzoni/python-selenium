contador = 0
numeros = [] 
while contador < 5: 
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    contador += 1

maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
        
print("Maior número:", maior)
