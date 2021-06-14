from ActionType import ActionType
from Resource import Resource
from Role import Role
from User import User


class RBACSystem:

    def __init__(self, users, resources, roles):
        self.__users = users
        self.__resources = resources
        self.__roles = roles

    def has_permissions(self, user, resource, action_type):

        user_roles = user.get_roles()
        for role in user_roles:
            if role.has_resource_access(resource, action_type):
                return True

        return False

    def get_roles(self):
        return self.__roles

    def get_users(self):
        return self.__users

    def get_resources(self):
        return self.__resources

    def assign_role_to_user(self, user, role):
        user.add_role(role)

    def remove_role_from_user(self, user, role):
        user.remove_role(role)

    def create_user(self, name):
        new_user = User(name)
        self.__users.append(new_user)