# 5 Autocomplete with Trie

As usual I've cut up the problem in two tasks

1. First we want to find out if the word exists inside of the list. If so we then mark it as **True**
2. After that I use a dictionary to store children of the node. After a short research, discovered that a dictionary is a pretty solid solution in terms of performance.

```text
Answer
Big O Notation Time: O(1)
Space: O(n)
```
