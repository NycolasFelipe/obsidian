# Mensagem de boas vindas e exibição do menu
print("------------Bem-vindos à Pizzaria do Nycolas Felipe Lourenço------------")
print("--------------------------------Cardápio--------------------------------")
print("------------------------------------------------------------------------")
print("---|    Tamanho    |    Pizza Salgada(PS)    |    Pizza Doce(PD)    |---")
print("---|       P       |        R$ 30.00         |       R$ 34.00       |---")
print("---|       M       |        R$ 45.00         |       R$ 48.00       |---")
print("---|       G       |        R$ 60.00         |       R$ 66.00       |---")
print("------------------------------------------------------------------------")

# Acumulador contendo valor total da compra
valor_total = 0

while True:
    # Input do sabor da pizza
    sabor = input("Entre com o sabor desejado (PS/PD): ")

    if sabor == "PS" or sabor == "PD":
        # Input do tamanho da pizza
        tamanho = input("Entre com o tamanho desejado (P/M/G): ")

        # Se tamanho e sabor válido, incrementa acumulador de valor total da pizza
        if tamanho == "P":
            if sabor == "PS":
                print("Você pediu uma pizza salgada no tamanho P: R$ 30.00")
                valor_total += 30
            elif sabor == "PD":
                print("Você pediu uma pizza doce no tamanho P: R$ 34.00")
                valor_total += 34
        
        elif tamanho == "M":
            if sabor == "PS":
                print("Você pediu uma pizza salgada no tamanho M: R$ 45.00")
                valor_total += 45
            elif sabor == "PD":
                print("Você pediu uma pizza doce no tamanho M: R$ 48.00")
                valor_total += 48

        elif tamanho == "G":
            if sabor == "PS":
                print("Você pediu uma pizza salgada no tamanho G: R$ 60.00")
                valor_total += 60
            elif sabor == "PD":
                print("Você pediu uma pizza doce no tamanho G: R$ 66.00")
                valor_total += 66
        else:
            # Retorna ao começo do loop caso tamanho seja inválido
            print("Tamanho inválido. Tente novamente.")
            print()
            continue

        print()

        # Continua o pedido caso o usuário queira pedir mais alguma coisa
        continuar_pedido = input("Deseja mais alguma coisa? (S/N): ")
        print()

        if continuar_pedido == "S":
            continue
        else:
            break

    else:
        # Retorna ao começo do loop caso sabor seja inválido
        print("Sabor inválido. Tente novamente.")
        print()
        continue

# Exibe mensagem final com o preço total do pedido
print(f"Valor total a ser pago: R$ {valor_total:.2f}")