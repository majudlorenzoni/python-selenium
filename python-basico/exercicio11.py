string = input('Digite uma string: ')

vogais = 'aeiouAEIOU'
string_sem_vogais = ""

for letra in string:
  if letra not in vogais:
    string_sem_vogais += letra

resultado = list(string_sem_vogais)
palavra = "palavra"
novo_resultado = []

for i in range(len(resultado)):
  novo_resultado.append(resultado[i])
  if i < len(resultado) - 1:
    novo_resultado.append(palavra)

print(''.join(novo_resultado))