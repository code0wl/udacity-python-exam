import datetime
import hashlib
from pprint import pprint


class Block:
    def __init__(self, date, data, previous_hash):
        self.date = date
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.encode(data)
        self.next = None

    def encode(self, data):
        str = data.encode('utf-8')
        sha = hashlib.sha256()
        sha.update(str)
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.size, self.head = 0, None

    def append(self, value):
        if not value:
            return

        self.size += 1
        item = self.head

        if not item:
            block = Block(datetime.datetime.now(), value, None)
            self.head = block
        else:
            while item.next:
                item = item.next
            item.next = Block(datetime.datetime.now(), value, item.hash)


# # Test 1 - Normal
# list = LinkedList()
# list.append('Manmeet')
# list.append('Singh')
# list.append('is')
# list.append('a')
# list.append('beta')
# list.append('tester')

# pprint(vars(list.head))
# pprint(vars(list.head.next))
# pprint(vars(list.head.next.next))
# pprint(vars(list.head.next.next.next))
# pprint(vars(list.head.next.next.next.next))
# pprint(vars(list.head.next.next.next.next.next))

# Test 2 - Edge None
list2 = LinkedList()
list2.append('Manmeet')
list2.append('Singh')
list2.append('is')
list2.append(None)
list2.append('beta')
list2.append('tester')

pprint(vars(list2.head))
pprint(vars(list2.head.next))
pprint(vars(list2.head.next.next))
pprint(vars(list2.head.next.next.next))
pprint(vars(list2.head.next.next.next.next))

# Test 3 - Edge False
list3 = LinkedList()
list3.append('Manmeet')
list3.append('Singh')
list3.append('is')
list3.append('a')
list3.append(False)
list3.append('tester')

pprint(vars(list3.head))
pprint(vars(list3.head.next))
pprint(vars(list3.head.next.next))
pprint(vars(list3.head.next.next.next))
pprint(vars(list3.head.next.next.next.next))
