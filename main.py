produtos = {}

def cadastra_produto(codigo,nome,preco,quantidade):
    if codigo in produtos:
        print(f'Produto {nome} ja esta cadastrado')
    else:
        produtos[codigo]={'nome':nome,'preco':preco,'quantidade':quantidade}

def buscar_produto(codigo):
    if codigo in produtos:
        for chave, valor in produtos[codigo].items():
            print(f'{chave}: {valor}')
    else:
        print(f'O produto de codigo {codigo} nao esta cadastrado.')
        
def atualizar(codigo, nome, preco, quantidade):
    if codigo in produtos:
        produtos[codigo] = {'nome' : nome, 'preço' : preco, 'quantidade' : quantidade}
    else:
        print(f'Nao existe produto com o codigo {codigo} na base')

def deleta(codigo):
    if codigo in produtos:
        del produtos[codigo]
        print(f'Produto de codigo {codigo} foi deletado')
    else:
        print(f'Nao existe produto com o codigo {codigo} na base')  

def lista():
    for produto in produtos.items():
        print(f'codigo = {produto[0]}')
        for chave, valor in produto[1].items():
            print(f'{chave}: {valor}')
        print('------------------\n')
                      
print ('Estoque esta iniciado')

while True:
  print('Digite qual operacao deseja fazer: ')
  print('1 - Criar no produto')
  print('2 - Buscar produto')
  print('3 - Atualizar produto ')
  print('4 - Deletar produto')
  print('5 - Listar produtos')
  print('6 - Finalizar estoque')
  a = int(input())
  if a == 1:
    print('Entre com codigo, nome, preco unitario e quantidade do produto ')
    codigo,nome,preco, quantidade =  input().split()
    codigo =  int(codigo)
    preco = float(preco)
    quantidade = int(quantidade)
    cadastra_produto(codigo, nome, preco, quantidade)
  if a == 2:
    print('Digite o codigo do produto')
    codigo =  int(input())
    buscar_produto(codigo)
  if a == 3:
    print('Entre com codigo, nome, preco unitario e quantidade do produto ')
    codigo,nome,preco, quantidade =  input().split()
    codigo =  int(codigo)
    preco = float(preco)
    quantidade = int(quantidade)
    cadastra_produto(codigo, nome, preco, quantidade)
  if a == 4:
    print('Digite o codigo do produto')
    codigo =  int(input())
    deleta(codigo)
  if a == 5:
    lista()
  if a == 6:
    break

print('Controle de estoque finalizado.')
