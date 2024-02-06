nome = input("Digite o nome do primeiro aluno: ")
media1 = float(input("Digite a sua média: "))
if media1 < 0 or media1 >10:
    media1 = float(input("Digite uma nota de 0 a 10: ")) 


nome = input("Digite o nome do segundo aluno: ")
media2 = float(input("Digite a sua média: "))
if media2 < 0 or media2 >10:
    media2 = float(input("Digite uma nota de 0 a 10: ")) 


nome = input("Digite o nome do terceiro aluno: ")
media3 = float(input("Digite a sua média: "))
if media3 < 0 or media3 >10:
    media3 = float(input("Digite uma nota de 0 a 10: ")) 


if media1 < media2 > media3:
    maior = media2
elif media2 < media3 > media1:
    maior = media3
else:
    maior = media1

print(f"O aluno {nome}, teve a maior média {maior}")