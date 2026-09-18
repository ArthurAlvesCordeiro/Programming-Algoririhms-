Idade = int(input("Qual a sua idade? "))
if Idade < 16:
    print("Por que você quer votar, vai brincar, você não tem idade ")

elif Idade == 16 or Idade == 17:
    print(" o seu voto é opcional volte mais tarde")
elif Idade >= 18 and Idade <= 69:
    print("O seu voto é obrigatório")
elif Idade >= 70:
    print("O seu voto é opcional, obrigado pro tudo")