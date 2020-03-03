class LRU_Cache(object):

    def __init__(self, capacity):
        self.limit = capacity
        self.cache_dictionary = {}
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        print(f'Getting', self.cache_dictionary[key])

    def set(self, key, value):
        if len(self.cache_dictionary) >= self.limit:
            return -1

        self.cache_dictionary.append(1, 1)
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        pass

    def hash_function(self, string):

        pass


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.get(1)

# our_cache.set(2, 2)
# our_cache.set(3, 3)
# our_cache.set(4, 4)


# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5)
# our_cache.set(6, 6)

# # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
# our_cache.get(3)
