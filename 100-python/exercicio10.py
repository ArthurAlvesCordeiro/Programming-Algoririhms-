salario = int(input("digite o salario: "))
totalVendido = int(input("digite o quanto vocé vendeu: "))

comissao = totalVendido * 4 / 100

totaSalario = salario + comissao

print(f" essa foi a sua comissão nesse mês: {comissao}")

print(f"esse foi o seu salario nesse mês: {totaSalario}")