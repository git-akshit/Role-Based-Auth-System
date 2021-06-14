from abc import abstractmethod

class Resource:
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def read(self):
        print(f"Reading {self.__name}")

    @abstractmethod
    def write(self):
        print(f"Writing {self.__name}")

    @abstractmethod
    def delete(self):
        print(f"Deleting in {self.__name}")

    def get_name(self):
        return self.__name