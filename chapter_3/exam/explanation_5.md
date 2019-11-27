## Time complexity:
Running the suffixes function will only visit each node in the trie
exactly one time, so the time complexity is O(n)

## Space complexity:
At each step we create a new list empty list. When we find a word we add
it to the list. Since for each node we copy the list the space
complexity is O(n * w) where n is the number of nodes and w the number of
words, the overall complexity is O(n^2)