nota = int(input("Digite sua nota: "))

while (nota < 0 or nota > 10):
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota = int(input("Digite sua nota: "))

print("Nota válida:", nota)