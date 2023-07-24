class Produto(object):
    def __init__(self, nome = None, valor = None):
        if nome is None:
            self.nome = input('Digite o nome do produto: ')
        else:
            self.nome = nome

        if valor is None:
            self.valor = float(input('Digite o valor do produto: '))
        else:
            self.valor = valor

