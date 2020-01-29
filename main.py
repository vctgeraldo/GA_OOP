#------------------------------#
#ALG. GENETICO ESCRITO EM OOP
#------------------------------#

class pop: 

    def __init__(self, size_pop, num_param):

        self.size_pop  = size_pop
        self.num_param = num_param

    def imprimir_pop(self):

        print(self.size_pop)

    def imprimirt_sum(self):

        print(self.num_param)
         


if __name__ == "__main__":
   
    a = pop(size_pop= 10, num_param= 3)
    

    a.imprimir_pop()

    #Bom dia eu sou muito inteligente para trabalhar com esse tipo de codigo
