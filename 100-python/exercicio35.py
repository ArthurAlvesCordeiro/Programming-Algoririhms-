idade = int(input("Idade: "))
estudante = input("Estudante: ").upper()

valor = 30.00

if idade < 12 or idade >= 60 or estudante == "SIM":
    valor = 15.00

print(f"\nValor do ingresso: R$ {valor:.2f}")