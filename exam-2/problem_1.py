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

print("Test 1 - Cache hit/miss")
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

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(3)

print("Test 2 - No Space Cache")
our_second_cache = LRU_Cache(0)
our_second_cache.set(1, 1)
print(our_second_cache.get(1), 'should return 10')

print("Test 3 - Setting multiple times on same key")
our_third_cache = LRU_Cache()
our_third_cache.set(2, 2)
our_third_cache.set(2, 1)
our_third_cache.set(2, 5)
our_third_cache.set(2, 10)

print(our_third_cache.get(2), 'should return 10')
