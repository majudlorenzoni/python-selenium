string = input("Digite algo: ")

vogais = ''
vogal = 0
if(string.count("a")):
    vogais += "a"
if(string.count("e")):
    vogais += "e"
if(string.count("i")):
    vogais += "i"
if(string.count("o")):
    vogais += "o"
if(string.count("u")):
    vogais += "u"

print("Vogais encontradas:", vogais)

frase = string.count(' ')
if (frase > 0):
    print("A string é uma frase.")
else:
    print("A string não é uma frase.")