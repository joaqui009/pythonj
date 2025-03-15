
class ContaBancaria:
    
    def __init__(self, saldo):
        self.saldo = saldo 
        
    def depositar(self, valor):
        self.saldo += valor
        # self.saldo + valor 
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True 
        else:
            return False
        
    def get_saldo(self):
        return self.saldo 
    
contajoaquim = ContaBancaria(6000)

contajoaquim.sacar(2000)

contajoaquim.depositar(240)

print(contajoaquim.get_saldo())

