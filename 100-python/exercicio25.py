Preco = float(input("Preço do produto: "))
Opcao = int(input("forma de pagamento escolha (1-4): "))

if Opcao == 1:
    ValorFinal = Preco - (Preco * 0.10)
    FormaPagamento = "Dinheiro ou Pix"

elif Opcao == 2:
    ValorFinal = Preco - (Preco * 0.05)
    FormaPagamento = "Débito"

elif Opcao == 3:
    ValorFinal = Preco
    FormaPagamento = "Crédito à vista"

elif Opcao == 4:
    ValorFinal = Preco + (Preco * 0.08)
    FormaPagamento = "Crédito parcelado"

print(f"Opção escolhida: {FormaPagamento}")
print(f"Valor final: R$ {ValorFinal:.2f}")