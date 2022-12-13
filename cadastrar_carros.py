

def criar_carro(carro):
  lista=[]
  lista.append(carro)

  return lista


n_carros = int(input ('Quantos carros deseja cadastrar? '))

nome=[]

for i in range(n_carros):
  
  nome.append(input('insira o carro '))


for i in list (nome):
  novo_carro= criar_carro(nome)

print(novo_carro)

print(novo_carro.__class__)