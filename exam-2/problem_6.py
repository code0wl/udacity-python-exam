class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def has_item(self, value):
        node = self.head

        while node:
            if node.get_value() == value:
                return True

            node = node.get_next_node()

        return False


def union(llist_1, llist_2):
    list = LinkedList()

    current = llist_1.head

    while current:
        value = current.get_value()

        if not list.has_item(value):
            list.append(value)

        current = current.next

    current = llist_2.head

    while current:
        value = current.get_value()
        if not list.has_item(value):
            list.append(value)

        current = current.next

    if list.size():
        return list

    return None


def intersection(llist_1, llist_2):
    list = LinkedList()
    current = llist_1.head

    while current:
        value = current.get_value()
        if llist_2.has_item(value) and not list.has_item(value):
            list.append(value)
        current = current.next

    if list.size():
        return list

    return None


# Specs
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
