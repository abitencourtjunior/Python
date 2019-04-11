class Idade:

    def __init__(self, idade):
        self._idade = idade

    def fuzzificacao(self):
        fuzzy = 1 / ( 1 + (((self._idade - 50) / 10).__pow__(2)))
        return fuzzy

    def defuzzificacao(self):
        verificacao = [0.05, 0.15, 0.30, 0.45, 0.60]
        fuzzy = round(self.fuzzificacao(), 4)
        if  (self._idade < 10 and fuzzy < verificacao[0]):
            print("Você é menor de idade")
        elif ( self._idade >= 18 and self._idade < 25 and fuzzy < verificacao[1]):
            print("Você é maior de idade, porém não adulto")
        elif ( self._idade > 25 and fuzzy < verificacao[2] ):
            print('Seu velho')

teste = Idade(int(input("Teste: ")))
teste.defuzzificacao()