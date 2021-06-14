from ActionType import ActionType
from Resource import Resource
import warnings


class Role:
    def __init__(self, name):
        self.__resource_privileges = {}
        self.__name = name

    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name 

    def add_resource_privileges(self, resource, privileges):
        if resource not in self.__resource_privileges:
            self.__resource_privileges[resource] = []

        for action_type in privileges:

            if action_type not in self.__resource_privileges[resource]:
                self.__resource_privileges[resource].append(action_type)

        return self

    def remove_resource_privileges(self, resource, privileges):
        if resource not in self.__resource_privileges:
            False

        for action_type in privileges:

            if action_type in self.__resource_privileges[resource]:
                self.__resource_privileges[resource].remove(action_type)

        return self

    def has_resource_access(self, resource, action_type):
        if resource not in self.__resource_privileges:
            return False

        if action_type in self.__resource_privileges[resource]:
            return True
        else:
            return False

