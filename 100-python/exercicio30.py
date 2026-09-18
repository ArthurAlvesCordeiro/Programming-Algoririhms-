# Aprovação de empréstimo

# Entrada de dados
valor_imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Prazo em anos: "))

# Calcula a prestação mensal
meses = anos * 12
prestacao = valor_imovel / meses

# Calcula o limite de 30% do salário
limite = salario * 0.30

# Mostra os resultados
print("\n--- RESULTADO ---")
print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")

# Verifica se o empréstimo foi aprovado
if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")