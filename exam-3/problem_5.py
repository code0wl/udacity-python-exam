class TrieNode:
    def __init__(self):
        self.is_found = False
        self.children = {}

    def insert(self, character):
        self.children[character] = TrieNode()

    def suffixes(self, suffix=''):
        suffixes = []

        for character, node in self.children.items():
            if node.is_found:
                suffixes.append(suffix + character)
            if node.children:
                suffixes += node.suffixes(suffix + character)

        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]

        node.is_found = True

    def find(self, prefix):
        node = self.root

        for character in prefix:
            if character not in node.children:
                return []
            node = node.children[character]

        return node


TreeInstance = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    TreeInstance.insert(word)

print("Test 1 - Normal")
print(TreeInstance.find("an").suffixes())
# ['t', 'thology', 'tagonist', 'tonym']
print(TreeInstance.find("fu").suffixes())  # ['n', 'nction']
print(TreeInstance.find("tri").suffixes())  # ['e', 'gger', 'gonometry', 'pod']

print("Test 1 - Edge return all if no entry")
print(TreeInstance.find("").suffixes())
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
