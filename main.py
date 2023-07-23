# questao 3
def imprimeLinha(char, quantidade):
    for i in range(quantidade):
        print(f'{char}', end='')

#questao 4
def imprimeAEsquerda(palavra, char, quantidade):
    tamanho_palavra = len(palavra)
    print(f'{palavra}', end='')
    imprimeLinha(char,quantidade - tamanho_palavra)

#questao 5
def imprimeADireita(palavra, char, quantidade):
    tamanho_palavra = len(palavra)
    imprimeLinha(char,quantidade - tamanho_palavra)
    print(f'{palavra}', end='')

#questao 6
def imprimeItemVenda(um_item_venda, produtos):
    #impressao do nome do produto a esquerda
    index_produto = um_item_venda[0]
    quantidade_produto = um_item_venda[1]
    imprimeAEsquerda(produtos[index_produto][0],' ',30)
    valor_multiplica_quantidade = f"{produtos[index_produto][1]} x {um_item_venda[1]}"
    imprimeAEsquerda(valor_multiplica_quantidade, ' ',12)
    #valor multiplica a quantidade
    subtotal = str(float(produtos[index_produto][1]) * int(um_item_venda[1]))
    imprimeADireita(subtotal,' ',8)

# questao 7
def novoProduto(lista_produtos):
    nome_produto = input('Digite o nome do produto: ')
    valor_produto = input('Digite o valor do produto: ')
    lista_produtos.append((nome_produto, valor_produto))
    return lista_produtos

# questao 8
def showMenu():
    imprimeLinha('*',50)
    print()

    imprimeADireita('MENU DE OPCOES',' ',18)
    print()

    imprimeLinha('*',50)
    print()

    print('0 - SAIR')
    print('1 - CADASTRAR NOVO PRODUTO')
    print('2 - REALIZAR VENDA')

    imprimeLinha('*',50)
    print()

    opcao = int(input('INFORME A SUA OPÇÃO: '))
    return opcao

# questao 9 total da compra
def calcularTotal(lista_item_venda, produtos):
    total = 0
    for item in lista_item_venda:
        total = total + int(produtos[item[0]][1]) * int(item[1])
    return total

# questao 10 nota fiscal
def notaFiscal(itens_venda, produtos):
    imprimeLinha('*',50)
    print()

    imprimeADireita('NOTA FISCAL',' ',30)
    print()

    imprimeLinha('*',50)
    print()

    for item in itens_venda:
        imprimeItemVenda(item, produtos)
        print()

    imprimeLinha('*',50)
    print()

    total = f'TOTAL: {calcularTotal(itens_venda, produtos)}'
    imprimeADireita(total, ' ', 50)
    print()

    imprimeLinha('*',50)
    print()

#questao 11 funcao auxiliar encontra produto
def procuraProduto(nome, produtos):
    for i, produto in enumerate(produtos):
        if produto[0] == nome:
            return i
    return -1

# questao 11 realizar VENDA
def realizarVenda(item_venda, produtos):
    nome_produto = input('Digite o nome do prod para add a venda')
    index_prod_enc = procuraProduto(nome_produto, produtos)

    if index_prod_enc < 0:
        print('PRODUTO NAO ENCONTRADO')
        return item_venda
    else:
        quantidade = input('Qual a quantidade do produto: ')
        item_venda.append((index_prod_enc,quantidade))
        return item_venda

def main():
    produtos = []
    item_venda = []
    opcao = -2
    while opcao != 0:
        opcao = showMenu()
        if opcao == 1:
            produtos = novoProduto(produtos)
        elif opcao == 2:
            item_venda = realizarVenda(item_venda, produtos)
    notaFiscal(item_venda, produtos)

main()
