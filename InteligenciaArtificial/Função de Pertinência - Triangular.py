import numpy as np

class fuzzy:

    def __init__(self, valor):
        self._valor = valor
        self._tringular = [10, 20, 30]

    def calcular_parametros(self):
        parametrox = (self._valor - self._tringular[0]) / (self._tringular[1] - self._tringular[0])
        parametroy = (self._tringular[2] - self._valor) / (self._tringular[2] - self._tringular[1])
        return [parametrox, parametroy]

    def funcao_tringular(self):
        fuzzyficacao = np.max(np.min(self.calcular_parametros()),0)
        print(fuzzyficacao)


teste = fuzzy(15)
print(teste.calcular_parametros())
teste.funcao_tringular()