class Pessoa:
    olhos = 2

    def __init__(self, nome=None, idade=34, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        #cumprimentar_da_classe=Pessoa.cumprimentar(self) pode gerar problemas se a classe "pai" for alterada.
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de Mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':

    jose = Mutante(nome='Jose', idade=2)
    maia = Pessoa('Maia', 30, jose)
    fabiano = Homem(nome='Fabiano', idade=5)
    maia = Pessoa('Maia', 30, fabiano)

    print(Pessoa.cumprimentar(maia))
    print(id(maia.nome))
    print('1', maia.cumprimentar())
    print(maia.nome, maia.idade)
    print(maia.idade)
    print(maia.filhos.count)

    maia.sobrenome = 'Ramalho'
    print('Nome completo', maia.nome, maia.sobrenome)

    del maia.filhos
    maia.olhos = 1

    print(maia.__dict__)
    print(fabiano.__dict__)

    print('Uma pessoa tem',Pessoa.olhos)
    print(maia.olhos)
    print(fabiano.olhos)
    print(id(Pessoa.olhos), id(maia.olhos), id(fabiano.olhos))

    print(Pessoa.metodo_estatico(), maia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), maia.nome_e_atributos_de_classe())

    print('Número de olhos do mutante', jose.nome ,'é',jose.olhos)

    print(maia.cumprimentar())
    print(fabiano.cumprimentar())
