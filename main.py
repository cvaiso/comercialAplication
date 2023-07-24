from menu import Menu
from produto import Produto
from venda import Venda


def main():
    menu = Menu()
    produtos = []
    vendas = []
    opcao = -2
    while opcao != 0:
        opcao = menu.principal()
        if opcao == 1:
            produtos.append(Produto())
        elif opcao == 2:
            venda = Venda()
            venda.realizarVenda(produtos)
            vendas.append(venda)
            venda.notaFiscal()

main()
