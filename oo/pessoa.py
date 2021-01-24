class Pessoa:
    def __init__(self, nome=None, idade=34, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':

    jose = Pessoa(nome='Jose', idade=2)
    maia = Pessoa('Maia', 30, jose)
    fabiano = Pessoa(nome='Fabiano', idade=5)
    maia = Pessoa('Maia', 30, fabiano)

    print(Pessoa.cumprimentar(maia))
    print(id(maia.nome))
    print('1', maia.cumprimentar())
    print(maia.nome, maia.idade)
    print(maia.idade)
    print(str(maia.filhos.count))

    for filho in maia.filhos:
        print(Pessoa.cumprimentar(filho.nome))

    for filho in maia.filhos:
        print(filho.nome)
