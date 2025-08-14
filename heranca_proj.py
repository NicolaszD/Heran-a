class BankAccount:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def deposit(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def withdraw(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def get_balance(self):
        return self.saldo


class CheckingAccount(BankAccount):
    def __init__(self, titular, saldo=0.0, limite_cheque_especial=500.0):
        super().__init__(titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def withdraw(self, valor):
        limite_total = self.saldo + self.limite_cheque_especial
        if valor <= limite_total:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            if self.saldo < 0:
                print(f"Atenção: você está utilizando R${-self.saldo:.2f} do cheque especial.")
        else:
            print("Saque não autorizado: valor excede o limite disponível (saldo + cheque especial).")
