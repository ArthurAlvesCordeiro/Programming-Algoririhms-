Ano = int(input("Esse ano e bissexto? Digite o ano: "))

if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print("O ano e bissexto")
else:
    print("O ano não e bissexto")