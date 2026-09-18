peso = float(input("Qual o seu peso? : "))
altura = float(input("Qual a sua altura? : "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print()
print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")