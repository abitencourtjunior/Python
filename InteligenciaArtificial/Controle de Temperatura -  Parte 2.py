import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Desclaração das váriaveis base
temperatura = ctrl.Antecedent(np.arange(0, 40, 18), 'temperatura')
umidade = ctrl.Antecedent(np.arange(0, 80, 10), 'umidade')
sensacao = ctrl.Consequent(np.arange(0, 70, 20), 'sensacao')

# Varivias Linguísticas
temperatura.automf(3)
umidade.automf(3)

# Funções Fuzzys

# Qualidade do Ar
sensacao['low'] = fuzz.trimf(sensacao.universe, [0, 0, 20])
sensacao['medium'] = fuzz.trimf(sensacao.universe, [0, 20, 70])
sensacao['high'] = fuzz.trimf(sensacao.universe, [20, 70, 70])

# Regras

rule1 = ctrl.Rule(temperatura['poor'] | umidade['good'], sensacao['high'])
rule2 = ctrl.Rule(temperatura['good'], sensacao['medium'])
rule3 = ctrl.Rule(temperatura['average'] | umidade['average'], sensacao['medium'])
rule4 = ctrl.Rule(temperatura['good'], sensacao['high'])


# Criando um sistema de Controle
sensacao_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
sensacaotipo = ctrl.ControlSystemSimulation(sensacao_ctrl)


sensacaotipo.input['temperatura'] = 6.5
sensacaotipo.input['umidade'] = 9.8

# Crunch the numbers
sensacaotipo.compute()

print(sensacaotipo.output['sensacao'])
sensacao.view(sim=sensacaotipo)