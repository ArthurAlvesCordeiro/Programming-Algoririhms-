precoProduto = float(input("digite o preço do produto: "))
quantidade = int(input("digite a quantidade comprada: "))
frete = float(input("digite o valor do frete: "))

subtotal = precoProduto * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {subtotal}")
print(f"Total: R$ {total}")