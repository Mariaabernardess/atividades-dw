
ana = 500.00
carlos = 300.00
maria = 100.00

def transferir(origem, destino, valor):
    if origem == destino:
        raise Exception("Não pode transferir para a própria conta!")

    if valor > origem[1]:
        raise Exception("Saldo insuficiente!")

    origem[1] -= valor
    destino[1] += valor
    
ana = ["Ana Lima", 500.00]
carlos = ["Carlos Souza", 300.00]
maria = ["Maria Silva", 100.00]

try:
    transferir(ana, carlos, 200.00)
    print("Ana transferiu R$ 200,00 para Carlos.")
except Exception as erro:
    print(erro)

try:
    transferir(carlos, maria, 150.00)
    print("Carlos transferiu R$ 150,00 para Maria.")
except Exception as erro:
    print(erro)

try:
    transferir(maria, ana, 500.00)
except Exception as erro:
    print("Erro:", erro)

try:
    transferir(ana, ana, 50.00)
except Exception as erro:
    print("Erro:", erro)

print("\nSaldos finais:")
print(ana[0], "R$", ana[1])
print(carlos[0], "R$", carlos[1])
print(maria[0], "R$", maria[1])
