class Menu():
    def principal(self):

        self.imprimeLinha('*', 50)
        print()

        self.imprimeADireita('MENU DE OPCOES',' ',18)
        print()

        self.imprimeLinha('*',50)
        print()

        print('0 - SAIR')
        print('1 - CADASTRAR NOVO PRODUTO')
        print('2 - REALIZAR VENDA')

        self.imprimeLinha('*',50)
        print()

        opcao = int(input('INFORME A SUA OPÇÃO: '))
        return opcao

    def imprimeLinha(self, char, quantidade):
        for i in range(quantidade):
            print(f'{char}', end='')

    def imprimeAEsquerda(self, palavra, char, quantidade):
        tamanho_palavra = len(palavra)
        print(f'{palavra}', end='')
        self.imprimeLinha(char,quantidade - tamanho_palavra)

    def imprimeADireita(self, palavra, char, quantidade):
        tamanho_palavra = len(palavra)
        self.imprimeLinha(char,quantidade - tamanho_palavra)
        print(f'{palavra}', end='')
