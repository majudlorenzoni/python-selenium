lista = [10, 40, 6, 4, 23, 54, 35, 42, 87, 90, 12, 22, 11, 3]
n = len(lista)
posicao = int(input("Digite uma posição de 0 a {}: ".format(n - 1)))

quartil = (posicao + 1) / n * 4

print(f"O quartil da posição {posicao} é: {quartil}")