from conta import Conta
from cliente import Cliente

t1 = Cliente('Yuri', 'Alberto', '13122299933')
t2 = Cliente('Memphis', 'Depay', '77777777')

c1 = Conta('123-4', t1,  120.0, 1000.0)
c2 = Conta('1-1', t2,  200.0, 10000.0 )

print(c1.titular.nome)
print(c2.titular.nome)

print(c1.titular.sobrenome)
print(c1.titular.cpf)

print(c1.__dict__)
print(c1.titular.__dict__)