from Role import Role


class User:
    def __init__(self, name):
        self.__roles = []
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_roles(self, roles):
        return self.__roles

    def get_roles(self):
        return self.__roles

    def add_role(self, role):
        
        self.__roles.append(role)
        return self

    def remove_role(self, role):
        if role in self.__roles:
            self.__roles.remove(role)
        else:
            raise (ValueError(f"User doesn't has {role} role"))

    
