# Boas vindas e inserção dos valores
print("Bem-vindo ao Sistema do Nycolas Felipe Lourenço")
valor_base = float(input("Informe o valor Base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

# Cálculo da porcentagem
porcentagem = 0

if idade < 19:
    porcentagem = 1
elif 19 <= idade and idade < 29:
    porcentagem = 1.50
elif 29 <= idade and idade < 39:
    porcentagem = 2.25
elif 39 <= idade and idade < 49:
    porcentagem = 2.40
elif 49 <= idade and idade < 59:
    porcentagem = 3.50
else:
    porcentagem = 6.00

# Cálculo do valor mensal
valor_mensal = valor_base * porcentagem

# Print valor do plano
valor_mensal = print(f"O valor mensal do plano é de: R$ {valor_mensal:.2f}")
