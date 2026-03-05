from POO_1.conta import Conta

conta = Conta('123-4', 'Marcello', 120.0, 1000.0)

#type(conta)
#print(conta.numero)
#print(conta.titular)
#print(conta.saldo)
#conta.depositar(50.0)
#print(conta.saldo)
print(conta.saldo)

consegui = conta.sacar(22)
if(consegui):
    print("Consegui sacar")
    print("Restam ainda: {}".format(conta.saldo))
else:
    print("Não consegui sacar")
    print("tenho apenas: {}".format(conta.saldo))