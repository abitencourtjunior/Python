from process import process
from manager import manager

teste = manager()

teste.execution_process(int(input("Caro usuário, informe quantos processos serão processados:  ")))
teste.show_list()
teste.remove_process_execution()