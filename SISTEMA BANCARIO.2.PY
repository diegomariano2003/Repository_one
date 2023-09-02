# Dicionário de usuários e senhas (Isso é apenas um exemplo, não use em produção!)
dicionario_usuarios = {
    "usuario1": {"senha": "375"},
    "usuario2": {"senha": "128"},
    "usuario3": {"senha": "339"},
    "usuario4": {"senha": "550"},
    "usuario5": {"senha": "111"}
}

# Função para verificar o usuário e senha
def verificar_credenciais(usuario, senha):
    if usuario in dicionario_usuarios and dicionario_usuarios[usuario]["senha"] == senha:
        return True
    else:
        return False
    
# menu principal
menu = """
Seja bem vindo ao Banco Unicenter do Python!

Por favor digite a opção desejada: 
[a] Entrar na minha conta 
[b] Preciso de ajuda
[c] Criar uma conta nova
[f] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "b":
        print("Certo, peço que entre em contato com nosso atendente: telefone (11) xxxx-xxxx")
        break

    elif opcao == "c":
        nome_do_novo_usuario = input("Digite seu nome completo: ")
        senha_do_novo_usuario = input("Digite uma senha (apenas números): ")
        dicionario_usuarios[nome_do_novo_usuario] = {"senha": senha_do_novo_usuario}
        print("Conta criada com sucesso!")

    elif opcao == "a":
        # Input do usuário
        usuario_input = input("Digite o nome de usuário: ")
        senha_input = input("Digite a senha: ")

        # Verificar credenciais
        if verificar_credenciais(usuario_input, senha_input):
            print("Acesso concedido. Bem-vindo,", usuario_input)
        else:
            print("Credenciais inválidas. Acesso negado.")

        menu_do_usuario = """
        [e] Extrato
        [s] Sacar
        [d] Depositar
        [p] Poupança
        [t] Transferir
        [f] Sair

        => """

        saldo = 1000
        extrato = ""
        numero_saques = 0
        poupanca = 0
        LIMITES_DE_SAQUES = 3

        while True:
            opcao = input(menu_do_usuario)

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

            elif opcao == "p":
                valor_para_poupanca = float(input("Digite o valor para transferir para a poupança: "))
                poupanca += valor_para_poupanca
                saldo -= valor_para_poupanca
                extrato += f"Transferido para a poupança R${valor_para_poupanca}\n"
                print(f"Saldo atual: R${saldo}\nSaldo da poupança: R${poupanca}")

            elif opcao == "t":
                valor_transferencia = float(input("Digite o valor para transferir: "))
                destinatario = input("Digite o nome do destinatário: ")
                if valor_transferencia <= saldo and destinatario in dicionario_usuarios:
                    saldo -= valor_transferencia
                    dicionario_usuarios[destinatario]["saldo"] += valor_transferencia
                    extrato += f"Transferência para {destinatario}: R${valor_transferencia}\n"
                    print(f"Transferência para {destinatario} concluída.")
                else:
                    print("Transferência não pode ser concluída. Verifique o saldo ou o destinatário.")

            elif opcao == "f":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")