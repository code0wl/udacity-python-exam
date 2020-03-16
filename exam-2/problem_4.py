# util
def is_user_in_group(user, group):
    return user == group.get_name() or user in group.get_users()


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent_user = "parent_user"
parent.add_user(parent_user)

child_user = "child_user"
child.add_user(child_user)


# Test cases

print("Test 1 - Normal")
print(is_user_in_group("sub_child_user", sub_child))  # True
print(is_user_in_group("parent_user", parent))  # True
print(is_user_in_group("child_user", child))  # True

print(is_user_in_group("parent_user", sub_child))  # False
print(is_user_in_group("", sub_child))  # False
print(is_user_in_group("sub_child_user", child))  # False

print("Test 2 - Edge Number")
print(is_user_in_group(123, sub_child))  # False

print("Test 3 - Edge Boolean")
print(is_user_in_group(True, child))  # False
