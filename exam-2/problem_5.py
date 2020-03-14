import datetime
import hashlib


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


# Test Cases
list = LinkedList()
list.append('someData1')
list.append('someData2')
list.append('someData3')
list.append('someData4')
list.append(None)

print(list.head.data)

blockChainOne = list.head.next
blockChainTwo = list.head.next.next

print(blockChainOne.hash == blockChainTwo.previous_hash)

print(blockChainTwo.data)
