import time
import datetime
from process import process

class manager(object):

    __list = []

    def __init__(self):
        self.__time_execution = datetime.datetime.now()

    def __add_process(self, process):
        self.__list.append(process)

    def __list_empty(self):
        if (len(self.__list)) == 0:
            return True
        return False

    def show_list(self):
        self.__order_priority()
        if (self.__list_empty()):
           print("Lista vazia!")
        print('--------------------------------------')
        for i in self.__list:
            print(i)
        print('--------------------------------------')

    def __order_priority(self):
        self.__list = sorted(self.__list, key=lambda process : process.priority)
        return self.__list

    def __remove_process(self):
        for i in self.__list:
            print(f'Executando o processo... PID: {i.pid}')
            while (i.ttl != 0):
                print(f'Priority: {i.priority} | TTL: {i.ttl} | Execution: {i.execution}')
                i.process_execution()
                i.process_start()
                time.sleep(2)
            self.show_list()

            if(i.ttl == 0):
                print('--------------------------------------')
                print(f'Encerrando o processo... PID: {i.pid} | Priority: {i.priority}')
                print(f'Tempo de Execução: {self.__time_process(i)}')
                print('--------------------------------------')
                self.__list.remove(i)
        time.sleep(3)

    def __time_process(self, process):
        return (datetime.datetime.now() - process.time)

    def execution_process(self, quantidade):
        for i in range(quantidade):
            process_teste = process()
            self.__add_process(process_teste)

    def remove_process_execution(self):
         while(len(self.__list) > 0):
            for i in range(len(self.__list)):
                self.__remove_process()
            print(f'Todos os processos foram encerrados, caro usuário - Tempo total: {(datetime.datetime.now() - self.__time_execution)}')





