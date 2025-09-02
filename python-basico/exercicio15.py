lista = [1, 2, 3, 4]

combinatoria = []
combinacoes_unicas = []
vistos = set()

for i in lista:
  for j in lista:
    combinatoria.append((i, j))

for a, b in combinatoria:
  t = tuple(sorted((a, b)))
  if t not in vistos:
    vistos.add(t)
    combinacoes_unicas.append((a, b))

print(combinacoes_unicas)
