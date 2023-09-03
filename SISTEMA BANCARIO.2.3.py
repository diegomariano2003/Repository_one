 #Dicionário de usuários e senhas
dicionario_usuarios = {
    "Diego": {"senha": "0605"},
    "Solange": {"senha": "1202"},
    "Thiago": {"senha": "1604"},
    "Guilherme": {"senha": "0602"},
    "Brutos": {"senha": "1111"}
}

# Função para verificar o usuário e senha
def verificar_credenciais(usuario, senha):
    if usuario in dicionario_usuarios and dicionario_usuarios[usuario]["senha"] == senha:
        return True
    else:
        return False

# Função para realizar um saque
def saque(valor, extrato, limite_saques, numero_saques):
    if numero_saques < limite_saques:
        if valor <= saldo:
            saldo -= valor
            extrato += f"Saque de R${valor}\n"
            numero_saques += 1
        else:
            print("Saldo insuficiente.")
    else:
        print("Limite de saques excedido.")
    return saldo, extrato

# Função para realizar um depósito
def deposito(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito de R${valor}\n"
    return saldo, extrato

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print(f"Extrato: R${saldo}\n{extrato}")

# Função para cadastrar um novo usuário
def cadastrar_usuario(CPF, nome, data_nascimento, endereco):
    global numero_conta
    numero_conta += 1
    dicionario_usuarios[nome] = {
        "CPF": CPF,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "conta_corrente": f"{numero_conta:04d}"
    }

# menu principal
menu = """
Seja bem vindo ao Banco Unicenter do Python!

É muito bom ter você aqui!

Por favor digite a opção desejada: 
[a] Entrar na minha conta 
[b] Preciso de ajuda
[c] Criar uma conta nova
[f] Sair

=> """

saldo = 1000
extrato = ""
numero_saques = 0
poupanca = 0
LIMITES_DE_SAQUES = 3
cheque_especial = 500
cheque_especial2 = 4000
numero_conta = 0

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
            break

        menu_do_usuario = """
        [e] Extrato
        [s] Sacar
        [d] Depositar
        [p] Poupança
        [t] Transferir
        [n] quero um novo serviço
        [f] Sair

        => """

        while True:
            opcao = input(menu_do_usuario)

            if opcao == "e":
                exibir_extrato(saldo, extrato)

            elif opcao == "s":
                saldo, extrato = saque(float(input("Digite o valor para sacar: ")), extrato, LIMITES_DE_SAQUES, numero_saques)

            elif opcao == "d":
                saldo, extrato = deposito(saldo, float(input("Digite o valor para depositar: ")), extrato)

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

            elif opcao == "n":
                menu22 = """
                Olá cliente Unicenter, feliz que queira contratar um novo plano.

                Temos algumas opções abaixo
                [a] viagem para a lua  - valor R$ 1.500
                [b] viagem para marte  - valor R$ 3.500
                [c] abrir um podcast   - valor R$ 100,00
                [d] doar dinheiro para o dono do banco - valor total da sua conta
                [e] extrato
                [f] voltar ao menu

                Obs: indicamos a opção a4, por ser generosa e social.

                => """
                
                while True:
                    opcao_servicos = input(menu22)

                    if opcao_servicos == "a":
                        viagem_lua = """
                        Parabéns! Sua viagem para a Lua foi comprada!
                        Em dez anos o projeto Artemis 50, sairá em direção ao seu destino.
                        Acompanhe pelo site: www.voupralua.com

                        ATENÇÃO: O BANCO UNICENTER NÃO TEM NENHUM LAÇO OU OBRIGAÇÃO COM O CONTRATO COM A EMPRESA LUNAR.
                        TODOS OS TERMOS E COBRANÇAS DEVERÃO SER FEITOS COM A EMPRESA RESPONSAVEL

                        Banco Unicenter agradece a transferência

                        Seu dinheiro, nossa alegria!
                        """
                        saldo += cheque_especial
                        saldo -= 1500
                        print (viagem_lua)
                        print(f"Saldo atual: R${saldo}\nValor utilizado de cheque especial R$ 500.00")

                    elif opcao_servicos == "b":
                        exiba = """
                        Parabéns! Sua viagem para Marte foi comprada!
                        Em dois anos o projeto Elo Musk 10, sairá em direção ao seu destino.
                        Acompanhe pelo site: www.voupramarte.com

                        ATENÇÃO: O BANCO UNICENTER NÃO TEM NENHUM LAÇO OU OBRIGAÇÃO COM O CONTRATO COM A EMPRESA MARCIANA.
                        TODOS OS TERMOS E COBRANÇAS DEVERÃO SER FEITOS COM A EMPRESA RESPONSAVEL

                        Banco Unicenter agradece a transferência

                        Seu dinheiro, nossa alegria!
                        """
                        saldo += cheque_especial2
                        saldo -= 3500
                        print (exiba)
                        print(f"Saldo atual: R${saldo}\nValor utilizado de cheque especial R$ 4000")

                    elif opcao_servicos == "c":
                        podcast = """
                        Parabéns! Seu podcast foi encomendado e será analisado pelos Estúdios Flow!

                        ATENÇÃO: O BANCO UNICENTER NÃO TEM NENHUM LAÇO OU OBRIGAÇÃO COM O CONTRATO COM O ESTÚDIO FLOW
                        TODOS OS TERMOS E COBRANÇAS DEVERÃO SER FEITOS COM A EMPRESA RESPONSAVEL

                        Banco Unicenter agradece a transferência

                        Seu dinheiro, nossa alegria!
                        """
                        saldo -= 100
                        print (podcast)
                        print(f"Saldo atual: R${saldo}")

                    elif opcao_servicos == "d":
                        doação = """
                        Parabéns! Doação feita!

                        ATENÇÃO: O BANCO UNICENTER NÃO TEM NENHUM LAÇO OU OBRIGAÇÃO COM O CONTRATO.
                        TODOS OS TERMOS E COBRANÇAS DEVERÃO SER FEITOS COM A EMPRESA RESPONSAVEL

                        Banco Unicenter agradece a doação.

                        Seu dinheiro, nossa alegria!
                        """
                        saldo -= saldo  # Doador está doando o valor total de sua conta
                        print (doação)
                        print("Doação concluída.")

                    elif opcao_servicos == "e":
                        exibir_extrato(saldo, extrato)

                    elif opcao_servicos == "f":
                        break

                    else:
                        print("Opção inválida. Tente novamente.")

            else:
                print("Opção inválida. Tente novamente.")
