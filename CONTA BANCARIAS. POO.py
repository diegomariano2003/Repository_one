class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"


class ContaBancaria:
    def __init__(self, numero_conta, cliente, saldo=0.0):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def consultar_saldo(self):
        return f"Saldo da conta {self.numero_conta}: R$ {self.saldo}"

    def __str__(self):
        return f"Conta Bancária - Número: {self.numero_conta}, Titular: {self.cliente.nome}"


# Exemplo de uso:
cliente1 = Cliente("João Silva", "123.456.789-00")
conta1 = ContaBancaria("001", cliente1)

cliente2 = Cliente("Maria Santos", "987.654.321-00")
conta2 = ContaBancaria("002", cliente2, 1000.0)

print(conta1)
print(conta2)

conta1.depositar(500.0)
conta1.sacar(200.0)

conta2.depositar(300.0)
conta2.sacar(150.0)

print(conta1.consultar_saldo())
print(conta2.consultar_saldo())
