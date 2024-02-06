j = input("Você está em jejum s/n? ")
t = input("Qual o nível de Triglicérides?")
t = int(t) # converter para inteiro 
if j == 's':
    if t > 150: 
        print ("Alto")
    else: 
        print ("Normal")
else:
    if t <  175:
        print ("Normal")
    else:
        print ("Alto")