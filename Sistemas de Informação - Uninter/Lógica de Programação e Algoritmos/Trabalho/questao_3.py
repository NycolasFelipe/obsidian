# Mensagem de boas-vindas
print("Bem-vindo à Madeireira do Lenhador Nycolas Felipe Lourenço")

# Função que retorna valor por tipo de madeira
def escolha_tipo():
    while True:
        print("Entre com o tipo de madeira desejado:")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        escolha = input(">> ")
        valor = 0
        
        if escolha == "PIN":
            valor = 150.4
        elif escolha == "PER":
            valor = 170.2
        elif escolha == "MOG":
            valor = 190.9
        elif escolha == "IPE":
            valor = 210.1
        elif escolha == "IMB":
            valor = 220.7
        else:
            # Em caso de valor inválido, pergunta novamente o tipo desejado
            print("Escolha inválida, entre com o modelo novamente.")
            print()
            continue

        print()
        return valor
    
# Função que calcula o desconto no preço das toras de acordo com a quantidade
def qtd_toras():
    while True:
        qtd = int(input("Entre com a quantidade de toras (m³): "))
        desconto = 0

        if qtd < 100:
            desconto = qtd
        elif qtd < 500:
            desconto = qtd * 0.96
        elif qtd < 1000:
            desconto = qtd * 0.91
        elif qtd <=2000:
            desconto = qtd * 0.84
        else:
            # Em caso de valor inválido, pergunta novamente a quantidade desejada
            print("Não aceitamos pedidos com essa quantidade de toras.")
            print("Por favor, entre com a quantidade novamente.")
            print()
            continue

        print()
        return desconto

# Função que calcula o preço de transporte
def transporte():
    while True:
        print("Escolha o tipo de transporte:")
        print("1 - Transporte Rodoviário  - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")

        escolha = input(">> ")
        valor = 0

        if escolha == "1":
            valor = 1000
        elif escolha == "2":
            valor = 2000
        elif escolha == "3":
            valor = 2500
        else:
            # Em caso de valor inválido, pergunta novamente o transporte desejado
            print("Escolha inválida, entre com o tipo de transporte novamente.")
            print()
            continue

        print()
        return valor

# Cálculo e exibição do valor final
valor_total = escolha_tipo() * qtd_toras() + transporte()
print(f"Total: R$ {valor_total:.2f}")
