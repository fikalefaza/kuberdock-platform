from kubedock.core import db
from kubedock.rbac.fixtures import add_permissions, Permission, Resource


# old rbac fixtures
RESOURCES = ("users", "nodes", "pods", "yaml_pods", "ippool",
             "notifications", "system_settings", "images", "predefined_apps")

ROLES = (
    ("Admin", False),
    ("User", False),
    ("LimitedUser", False),
    ("TrialUser", False),
    ("HostingPanel", True),
)

PERMISSIONS = (
    # Admin
    ("users", "Admin", "create", True),
    ("users", "Admin", "get", True),
    ("users", "Admin", "edit", True),
    ("users", "Admin", "delete", True),
    ("users", "Admin", "auth_by_another", True),
    ("nodes", "Admin", "create", True),
    ("nodes", "Admin", "get", True),
    ("nodes", "Admin", "edit", True),
    ("nodes", "Admin", "delete", True),
    ("nodes", "Admin", "redeploy", True),
    ("pods", "Admin", "create", False),
    ("pods", "Admin", "get", False),
    ("pods", "Admin", "edit", False),
    ("pods", "Admin", "delete", False),
    ("yaml_pods", "Admin", "create", False),
    ("ippool", "Admin", "create", True),
    ("ippool", "Admin", "get", True),
    ("ippool", "Admin", "edit", True),
    ("ippool", "Admin", "delete", True),
    ("ippool", "Admin", "view", True),
    ("notifications", "Admin", "create", True),
    ("notifications", "Admin", "get", True),
    ("notifications", "Admin", "edit", True),
    ("notifications", "Admin", "delete", True),
    ("system_settings", "Admin", "read", True),
    ("system_settings", "Admin", "write", True),
    ("system_settings", "Admin", "delete", True),
    ("images", "Admin", "get", True),
    ("images", "Admin", "isalive", True),
    ("predefined_apps", "Admin", "create", True),
    ("predefined_apps", "Admin", "get", True),
    ("predefined_apps", "Admin", "edit", True),
    ("predefined_apps", "Admin", "delete", True),
    # User
    ("users", "User", "create", False),
    ("users", "User", "get", False),
    ("users", "User", "edit", False),
    ("users", "User", "delete", False),
    ("users", "User", "auth_by_another", False),
    ("nodes", "User", "create", False),
    ("nodes", "User", "get", False),
    ("nodes", "User", "edit", False),
    ("nodes", "User", "delete", False),
    ("nodes", "User", "redeploy", False),
    ("pods", "User", "create", True),
    ("pods", "User", "get", True),
    ("pods", "User", "edit", True),
    ("pods", "User", "delete", True),
    ("yaml_pods", "User", "create", True),
    ("ippool", "User", "create", False),
    ("ippool", "User", "get", False),
    ("ippool", "User", "edit", False),
    ("ippool", "User", "delete", False),
    ("ippool", "User", "view", False),
    ("notifications", "User", "create", False),
    ("notifications", "User", "get", False),
    ("notifications", "User", "edit", False),
    ("notifications", "User", "delete", False),
    ("images", "User", "get", True),
    ("images", "User", "isalive", True),
    ("predefined_apps", "User", "create", False),
    ("predefined_apps", "User", "get", True),
    ("predefined_apps", "User", "edit", False),
    ("predefined_apps", "User", "delete", False),
    # LimitedUser
    ("users", "LimitedUser", "create", False),
    ("users", "LimitedUser", "get", False),
    ("users", "LimitedUser", "edit", False),
    ("users", "LimitedUser", "delete", False),
    ("users", "LimitedUser", "auth_by_another", False),
    ("nodes", "LimitedUser", "create", False),
    ("nodes", "LimitedUser", "get", False),
    ("nodes", "LimitedUser", "edit", False),
    ("nodes", "LimitedUser", "delete", False),
    ("nodes", "LimitedUser", "redeploy", False),
    ("pods", "LimitedUser", "create", False),
    ("pods", "LimitedUser", "get", True),
    ("pods", "LimitedUser", "edit", True),
    ("pods", "LimitedUser", "delete", True),
    ("yaml_pods", "LimitedUser", "create", True),
    ("ippool", "LimitedUser", "create", False),
    ("ippool", "LimitedUser", "get", False),
    ("ippool", "LimitedUser", "edit", False),
    ("ippool", "LimitedUser", "delete", False),
    ("ippool", "LimitedUser", "view", False),
    ("notifications", "LimitedUser", "create", False),
    ("notifications", "LimitedUser", "get", False),
    ("notifications", "LimitedUser", "edit", False),
    ("notifications", "LimitedUser", "delete", False),
    ("images", "LimitedUser", "get", True),
    ("images", "LimitedUser", "isalive", True),
    ("predefined_apps", "LimitedUser", "create", False),
    ("predefined_apps", "LimitedUser", "get", True),
    ("predefined_apps", "LimitedUser", "edit", False),
    ("predefined_apps", "LimitedUser", "delete", False),
    # TrialUser
    ("users", "TrialUser", "create", False),
    ("users", "TrialUser", "get", False),
    ("users", "TrialUser", "edit", False),
    ("users", "TrialUser", "delete", False),
    ("users", "TrialUser", "auth_by_another", False),
    ("nodes", "TrialUser", "create", False),
    ("nodes", "TrialUser", "get", False),
    ("nodes", "TrialUser", "edit", False),
    ("nodes", "TrialUser", "delete", False),
    ("nodes", "TrialUser", "redeploy", False),
    ("pods", "TrialUser", "create", True),
    ("pods", "TrialUser", "get", True),
    ("pods", "TrialUser", "edit", True),
    ("pods", "TrialUser", "delete", True),
    ("yaml_pods", "TrialUser", "create", True),
    ("ippool", "TrialUser", "create", False),
    ("ippool", "TrialUser", "get", False),
    ("ippool", "TrialUser", "edit", False),
    ("ippool", "TrialUser", "delete", False),
    ("ippool", "TrialUser", "view", False),
    ("notifications", "TrialUser", "create", False),
    ("notifications", "TrialUser", "get", False),
    ("notifications", "TrialUser", "edit", False),
    ("notifications", "TrialUser", "delete", False),
    ("images", "TrialUser", "get", True),
    ("images", "TrialUser", "isalive", True),
    ("predefined_apps", "TrialUser", "create", False),
    ("predefined_apps", "TrialUser", "get", True),
    ("predefined_apps", "TrialUser", "edit", False),
    ("predefined_apps", "TrialUser", "delete", False),
    # HostingPanel
    ("users", "HostingPanel", "create", False),
    ("users", "HostingPanel", "get", False),
    ("users", "HostingPanel", "edit", False),
    ("users", "HostingPanel", "delete", False),
    ("users", "HostingPanel", "auth_by_another", False),
    ("nodes", "HostingPanel", "create", False),
    ("nodes", "HostingPanel", "get", False),
    ("nodes", "HostingPanel", "edit", False),
    ("nodes", "HostingPanel", "delete", False),
    ("nodes", "HostingPanel", "redeploy", False),
    ("pods", "HostingPanel", "create", False),
    ("pods", "HostingPanel", "get", False),
    ("pods", "HostingPanel", "edit", False),
    ("pods", "HostingPanel", "delete", False),
    ("yaml_pods", "HostingPanel", "create", False),
    ("ippool", "HostingPanel", "create", False),
    ("ippool", "HostingPanel", "get", False),
    ("ippool", "HostingPanel", "edit", False),
    ("ippool", "HostingPanel", "delete", False),
    ("ippool", "HostingPanel", "view", False),
    ("notifications", "HostingPanel", "create", False),
    ("notifications", "HostingPanel", "get", False),
    ("notifications", "HostingPanel", "edit", False),
    ("notifications", "HostingPanel", "delete", False),
    ("images", "HostingPanel", "get", True),
    ("images", "HostingPanel", "isalive", True),
    ("predefined_apps", "HostingPanel", "create", False),
    ("predefined_apps", "HostingPanel", "get", True),
    ("predefined_apps", "HostingPanel", "edit", False),
    ("predefined_apps", "HostingPanel", "delete", False),
)



def upgrade(upd, with_testing, *args, **kwargs):
    upd.print_log('Update permissions...')
    Permission.query.delete()
    Resource.query.delete()
    add_permissions()
    db.session.commit()


def downgrade(upd, with_testing, exception, *args, **kwargs):
    upd.print_log('Downgrade permissions...')
    Permission.query.delete()
    Resource.query.delete()
    add_permissions()
    db.session.commit()
