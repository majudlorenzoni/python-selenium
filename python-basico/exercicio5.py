nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print("Sua média é:", media)
if (media == 10):
    print("Aprovado com distinção")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")