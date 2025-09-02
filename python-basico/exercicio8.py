data = input("Digite sua data de nascimento (dd/mm/aaaa): ")


data = data.split('/')

dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

print("Você nasceu em", dia, "do", mes, "de", ano)