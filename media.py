nome = input("Digite o seu nome: ")
prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
trabalho = float(input("Digite a nota do trabalho: "))

if prova1 < 0 or prova1 >10:
    prova1 = float(input("Digite uma nota de 0 a 10: "))   
if prova2 < 0 or prova1 >10:
    prova2 = float(input("Digite uma nota de 0 a 10: ")) 
if trabalho < 0 or prova1 >10:
    trabalho = float(input("Digite uma nota de 0 a 10: ")) 

media = prova1*0.35 + prova2*0.35 + trabalho*0.3

if media >= 5:
    situacao = 'Aprovado'
elif media >= 3.5:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

print(f"Olá, {nome} sua média final foi {media} situação: {situacao}")