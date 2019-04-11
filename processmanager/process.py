from random import randint

class process(object):

    def __init__(self):
        self.__pid = self.__generate_process_random(1000, 9999)
        self.__ttl = self.__generate_process_random(0, 5)
        self.__priority = self.__generate_process_random(0, 4)
        self.__execution = False

    @property
    def pid(self):
        return self.__pid

    @property
    def ttl(self):
        return self.__ttl

    @property
    def priority(self):
        return self.__priority

    @property
    def execution(self):
        return self.__execution

    def process_execution(self):
        self.__ttl -= 1

    def process_start(self):
        self.__execution = True

    def __generate_process_random(self, init, finish):
        return randint(init, finish)

    def __str__(self):
        return f'| PID: {self.__pid} | Priority: {self.__priority} | TTL: {self.__ttl} | Execution: {self.__execution} '