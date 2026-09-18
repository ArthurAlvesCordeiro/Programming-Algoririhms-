mes = int(input("Digite o mês (1 a 12): "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")
elif mes == 2:
    # Verifica se o ano é bissexto
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print("29 dias")
    else:
        print("28 dias")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    print("31 dias")
else:
    print("30 dias")