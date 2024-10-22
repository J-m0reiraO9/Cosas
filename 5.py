class Cuenta():
    def __init__(self, nombre, banco, saldo):
        self.__nombre = nombre
        self.__banco = banco
        self.__saldo = saldo
        
        
    def get_nombre(self):
        return self.__nombre
        
    def get_banco(self):
        return self.__banco
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
Total = Cuenta("Miguel", "BNC", 400)

print(Total.get_banco())
Total.set_saldo(5000)
print(Total.get_saldo())
