import numpy

class Altura:


    triangulo = []

    def __init__(self, altura):
        self._altura = altura

    def fuzzificacao(self):
        self.min.append(1.45 - self._altura)
        self.min.append(2.00 - self._altura)
        self.max.append(0)
        self.max.append(numpy.amin(self.min))
        fuzzy = numpy.amax(self.max)
        # fuzzy = max[min[self._altura - 1.45, self._altura - 2.00], 0]
        print(fuzzy)


#teste = Altura(1.56)
#teste.fuzzificacao()