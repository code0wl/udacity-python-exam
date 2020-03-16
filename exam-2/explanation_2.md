# 2

First time I have done this excersize, was when I was learning node.js
Here I just loop if the file is found and just print it if it's found. I do this by checking for each file in the tree, then recursively call the function again, making use of recursion, of course.

I think the complexity is Big O of N times for the total number of directories found in the tree.

The space complexity is different as it could grow exponentially with every recursive operation.

```text
Answer
Big O Notation Time: O(n)
Space: O(n log n)
```
