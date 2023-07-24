from menu import Menu

class Venda(Menu):
    def __init__ (self):
        self.produtos_da_venda = []
        self.quantidades = []
        self.total = 0

    def realizarVenda(self, produtos):
        nome_produto = None
        while nome_produto != '':
            nome_produto = input('Nome do prod a ser adicionado a venda: ')
            if nome_produto == '':
                break
            prod_enc = self.procuraProduto(nome_produto, produtos)

            if prod_enc == None:
                print('PRODUTO NAO ENCONTRADO')
            else:
                quantidade = int(input('Qual a quantidade do produto: '))
                self.produtos_da_venda.append(prod_enc)
                self.quantidades.append(quantidade)

    def procuraProduto(self, nome, produtos):
        for produto in produtos:
            if produto.nome == nome:
                return produto
        return None

    def notaFiscal(self):
        menu = Menu()
        menu.imprimeLinha('*',50)
        print()

        menu.imprimeADireita('NOTA FISCAL',' ',30)
        print()

        menu.imprimeLinha('*',50)
        print()

        for produto, quantidade in zip(self.produtos_da_venda, self.quantidades):
            self.imprimeItemVenda(produto, quantidade)
            print()

        menu.imprimeLinha('*',50)
        print()

        total = f'TOTAL: {self.calcularTotal()}'
        menu.imprimeADireita(total, ' ', 50)
        print()

        menu.imprimeLinha('*',50)
        print()

    def imprimeItemVenda(self, produto, quantidade):
        menu = Menu()
        #impressao do nome do produto a esquerda
        menu.imprimeAEsquerda(produto.nome,' ',30)
        valor_multiplica_quantidade = f"{produto.valor} x {quantidade}"
        menu.imprimeAEsquerda(valor_multiplica_quantidade, ' ',12)
        #valor multiplica a quantidade
        subtotal = str(produto.valor * quantidade)
        menu.imprimeADireita(subtotal,' ',8)

    def calcularTotal(self, produtos = None, quantidades = None):
        if produtos == None and quantidades == None:
            total = 0
            for produto,quantidade in zip(self.produtos_da_venda, self.quantidades):
                total = total + float(produto.valor) * int(quantidade)
            return total
        else:
            total = 0
            for produto,quantidade in produtos, quantidades:
                    total = total + float(produto.valor) * int(quantidade)
            return total
