menu = """
[e] Extrato
[s] Sacar
[d] Depositar
[f] Sair

=> """

saldo = 1000
limite = 1000
extrato = ""
numero_saques = 0
LIMITES_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "e":
        print(f"Extrato: R${saldo}\n{extrato}")

    elif opcao == "s":
        if numero_saques < LIMITES_DE_SAQUES:
            valor_saque = float(input("Digite o valor para sacar: "))
            if valor_saque <= saldo:
                saldo -= valor_saque
                extrato += f"Saque de R${valor_saque}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques excedido.")

    elif opcao == "d":
        valor_deposito = float(input("Digite o valor para depositar: "))
        saldo += valor_deposito
        extrato += f"Depósito de R${valor_deposito}\n"

    elif opcao == "f":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")