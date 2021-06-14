from CommandLineInterface import CommandLineInterface
from RBACSystem import RBACSystem
from Resource import Resource
from Role import Role
from User import User
from ActionType import ActionType

if __name__ == '__main__':

    #Creating reosurces
    compute_engine = Resource("Compute Engine")
    vm = Resource("VM")
    snapshot = Resource("Snapshot")

    #Creating roles
    role_read_compute_engine = Role("Role Read Compute Engine").add_resource_privileges(compute_engine, [ActionType.READ])
    role_compute_engine = Role("Role Compute Engine Full Access").add_resource_privileges(compute_engine,
                                                              [ActionType.READ, ActionType.WRITE, ActionType.DELETE])

    role_read_vm = Role("Role Read VM").add_resource_privileges(vm, [ActionType.READ])
    role_vm = Role("Role VM Full Access").add_resource_privileges(vm,
                                                                  [ActionType.READ, ActionType.WRITE,
                                                                   ActionType.DELETE])

    role_read_snapshot = Role("Role Read Snapshots").add_resource_privileges(snapshot,[ActionType.READ,])
    role_snapshot = Role("Role Snapshots Full Access").add_resource_privileges(snapshot,
                                                                                [ActionType.READ, ActionType.WRITE])

    #Creating User
    admin_user = User("Admin User").add_role(role_compute_engine).add_role(role_vm).add_role(role_snapshot)
    read_user = User("Read user").add_role(role_read_compute_engine).add_role(role_read_vm).add_role(
        role_snapshot)

    #initializing RBAC System
    users = [admin_user, read_user]
    roles = [role_read_compute_engine, role_compute_engine, role_read_vm, role_vm, role_read_snapshot,
             role_snapshot]
    resources = [compute_engine, vm, snapshot]

    rbac_system = RBACSystem(users=users, roles=roles, resources=resources)

    cli = CommandLineInterface(rbac_system)
    cli.execute_cli()
