lista = [10, 20, 30, 40, 50]

def calcular_mediana(lista):
    menor_valor = min(lista)
    maior_valor = max(lista)

    dispersao = maior_valor - menor_valor
    print("Dispersão:", dispersao)
    return dispersao

calcular_mediana(lista)
