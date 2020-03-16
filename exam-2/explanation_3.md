# 3

After researching online. I found a tree was the most efficient solution.
So the tree accumulates the letters and the sum of occurrences.

I check first to see if the values being passed are valid by checking if its not empty or not a string. Once the argument has passed these conditions. So, I calculate the occurrences of each character passed in the data string, then I sort and encode it.

For decoding I follow a similar process. Big differences is I return one string instead of the string and a tree.

```text
Answer
Big O Notation Time: O(n log n)
Space Complexity: O(log n)
```
