# 1

I've used OrderedDict as cache, this tracks entries in an ordered way.
Reason why is if a key is mutated, the location of the key does not change.

Makes it very easy to just change the value and keep the key in place

```text
Answer
Big O Notation Time: O(1)
Space: O(n)
```
