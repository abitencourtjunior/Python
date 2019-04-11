class trapeziodal:

    def __init__(self, valor):
        self._valor = valor
        self._tringular = [10, 12, 20, 30]

    def calcular_parametros(self):
        parametrox = (self._valor - self._tringular[0]) / (self._tringular[1] - self._tringular[0])
        parametroy = (self._tringular[3] - self._valor) / (self._tringular[3] - self._tringular[2])
        return [parametrox, 1, parametroy]

    def funcao_tringular(self):
        fuzzyficacao = np.max(np.min(self.calcular_parametros()),0)
        print(fuzzyficacao)