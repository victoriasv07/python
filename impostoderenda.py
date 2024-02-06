s = float(input("Digite seu salário: "))
t = 00

if s < 2112:
    print("Você é isento de pagar o imposto de renda")

elif s <2826.65:
    t = 0.075

elif s <3751.05:
    t = 0.15

elif s <4664.68:
    t = 0.225

else:
    t = 0.275


ir = s*t
print(f"Você pagará {ir} de imposto de renda")