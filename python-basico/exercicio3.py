area = float(input('Digite a area que você pretende pintar: '))

litro = area / 3

lata = int(litro / 18)

if litro % 18 != 0:
  lata += 1
  
preço = lata * 80

print(f'O custo total para pintar a área de {area}m² é de R${preço:.2f}.')
