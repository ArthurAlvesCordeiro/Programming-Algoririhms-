VolerUm = int(input("Digite o primeiro valor: "))
VolerDois = int(input("Digite o segundo valor: "))
VolerTres = int(input("Digite o terceiro valor: "))

if VolerUm > VolerDois and VolerUm > VolerTres:
    print(f"O primeiro valor {VolerUm} é maior que os outros dois.")
elif VolerDois > VolerUm and VolerDois > VolerTres:
    print(f"O segundo valor {VolerDois} é maior que os outros dois.")
else:
    print(f"O terceiro valor {VolerTres} é maior que os outros dois.")

if VolerUm < VolerDois and VolerUm < VolerTres:
    print(f"O primeiro valor {VolerUm} é menor que os outros dois.")    
elif VolerDois < VolerUm and VolerDois < VolerTres:
    print(f"O segundo valor {VolerDois} é menor que os outros dois.")    
else:
    print(f"O terceiro valor {VolerTres} é menor que os outros dois.")    