from collections import OrderedDict


class LRU_Cache():
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache.keys():
            value = self.cache.pop(key)
            self.cache[key] = value
            print("returning", value)
            return value
        else:
            print(key, "not found, returning -1")
            return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity and self.capacity <= 0:
            return -1

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return True
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
        return True

# Tests


print("Test 1 - Cache hit")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print("Test 2 - Cache miss")
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(3)

print("Test 3 - Miscellaneous")
our_cache1 = LRU_Cache()
our_cache1.set(1, 1)
our_cache1.set(4, 1)
our_cache1.set(2, 2)
our_cache1.set(3, 1)
our_cache1.set(10, 1)
our_cache1.set(9, 10)
our_cache1.set(19, 100)

print(our_cache1.get(4), 'should return 1')
print(our_cache1.get(5), 'should return -1')
print(our_cache1.get(9), 'should return 10')
print(our_cache1.get(19), 'should return 100')
