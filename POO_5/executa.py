from conta import Conta
from cliente import Cliente

t1 = Cliente('Yuri', 'Alberto', '13122299933')
t2 = Cliente('Memphis', 'Depay', '77777777')

c1 = Conta('123-4', t1,  120.0, 1000.0)
c2 = Conta('1-1', t2,  200.0, 10000.0 )

c1.depositar(1000.0)
c1.extrato()
c1.sacar(200.0)
c1.extrato()
c2.transfere(c1, 1500.0)
c1.extrato()
c2.extrato()
c1.historico.imprime()