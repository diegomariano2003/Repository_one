import sqlite3

# Classe para representar a tabela Cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

# Classe para representar a tabela Conta
class Conta:
    def __init__(self, numero_conta, saldo, cliente_id):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.cliente_id = cliente_id

# Classe para a API de Integração com SQLite
class BancoSQLite:
    def __init__(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Conta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_conta TEXT NOT NULL UNIQUE,
                saldo REAL,
                cliente_id INTEGER,
                FOREIGN KEY (cliente_id) REFERENCES Cliente (id)
            )
        ''')
        self.conn.commit()

    def adicionar_cliente(self, cliente):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO Cliente (nome, cpf) VALUES (?, ?)', (cliente.nome, cliente.cpf))
        self.conn.commit()
        return cursor.lastrowid

    def adicionar_conta(self, conta):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO Conta (numero_conta, saldo, cliente_id) VALUES (?, ?, ?)', (conta.numero_conta, conta.saldo, conta.cliente_id))
        self.conn.commit()

    def buscar_cliente_por_cpf(self, cpf):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Cliente WHERE cpf = ?', (cpf,))
        cliente_data = cursor.fetchone()
        if cliente_data:
            return Cliente(cliente_data[1], cliente_data[2])
        return None

    def buscar_conta_por_numero(self, numero_conta):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Conta WHERE numero_conta = ?', (numero_conta,))
        conta_data = cursor.fetchone()
        if conta_data:
            return Conta(conta_data[1], conta_data[2], conta_data[3])
        return None

    def fechar_conexao(self):
        self.conn.close()

# Exemplo de uso:
if __name__ == '__main__':
    banco = BancoSQLite('banco.db')

    cliente1 = Cliente('João Silva', '123.456.789-00')
    cliente_id = banco.adicionar_cliente(cliente1)

    conta1 = Conta('001', 1000.0, cliente_id)
    banco.adicionar_conta(conta1)

    cliente2 = Cliente('Maria Santos', '987.654.321-00')
    cliente_id = banco.adicionar_cliente(cliente2)

    conta2 = Conta('002', 500.0, cliente_id)
    banco.adicionar_conta(conta2)

    # Buscar cliente por CPF
    cpf = '123.456.789-00'
    cliente = banco.buscar_cliente_por_cpf(cpf)
    if cliente:
        print(f'Cliente encontrado: {cliente.nome}')

    # Buscar conta por número
    numero_conta = '002'
    conta = banco.buscar_conta_por_numero(numero_conta)
    if conta:
        print(f'Conta encontrada: Número: {conta.numero_conta}, Saldo: {conta.saldo}')

    banco.fechar_conexao()

