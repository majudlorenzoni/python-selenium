numero_real = input('Digite um número real: ')

resultado = numero_real.partition('.')
resultado = (resultado[0], resultado[1], resultado[2])
numero_final = resultado[2]

print("resultado:", numero_final)