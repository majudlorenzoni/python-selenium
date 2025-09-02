lista = [10, 40, 6, 4, 23, 54, 35, 42, 87, 90, 12, 22, 11, 3]
sorted_lista = sorted(lista)

mediana = len(sorted_lista) / 2

if len(sorted_lista) % 2 == 0:
  mediana = (sorted_lista[int(mediana) - 1] + sorted_lista[int(mediana)]) / 2
elif len(sorted_lista) % 2 != 0:
  mediana = sorted_lista[int(mediana)]


print(mediana)
