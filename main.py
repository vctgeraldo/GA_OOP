#----------------------------------------------------------------------------#
#ALG. GENETICO ESCRITO EM OOP
#Autor:Victor Coelho Geraldo
#
#Data: 18 de fevereiro de 2020
#----------------------------------------------------------------------------#

class InceriValorNaLista:

    def __init__(self, lista, valor_adicionado):

        self.lista            = lista
        self.valor_adicionado = valor_adicionado

        print('iniciando classe...')

    def ImprimirLista(self):

        for contador in self.lista:

            print(contador)

    def AdicionarItemNaLista(self):

        self.lista.append(self.valor_adicionado)


if __name__ == "__main__":
   
    a = InceriValorNaLista([1,2,3], 'victor')

    a.ImprimirLista()
    print()
    a.AdicionarItemNaLista()
    print()
    a.ImprimirLista()

   
