from random import randint
import datetime

class process(object):

    def __init__(self):
        self.__pid = self.__generate_process_random(1000, 9999)
        self.__ttl = self.__generate_process_random(0, 5)
        self.__priority = self.__generate_process_random(0, 4)
        self.__size = self.__generate_process_random(0, 1000)
        self.__time = datetime.datetime.now()
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

    @property
    def time(self):
        return self.__time

    def process_execution(self):
        self.__ttl -= 1

    def process_start(self):
        self.__execution = True

    def __generate_process_random(self, init, finish):
        return randint(init, finish)

    def __str__(self):
        return f'| PID: {self.__pid} | Priority: {self.__priority} | TTL: {self.__ttl} | Size: {self.__size} Bytes | Time: {self.__time.strftime("%Y-%m-%d %H:%M:%S %z")} | Execution: {self.__execution} '