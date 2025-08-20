produtos = (
    ("arroz", 5.99),
    ("feijão", 6.99),
    ("macarrão", 7.99),
    ("açúcar", 4.99),
    ("sal", 2.99),
)

print("Produtos Disponiveis")

for nome, preco in produtos:
    print(f"{nome:.<20}: R$ {preco:.2f}")