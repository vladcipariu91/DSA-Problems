## Time complexity:
If the list is empty then the return value will be (None, None)
If the list only has one element we'll return a pair with that element as both
the min and the max.
Otherwise we determine the min and max from the first two elements in the array.
We start iterating from the second position until the end of the array comparing
the element at the current position against min and max.

Since we only iterate once over the array the time complexity is O(n) 

## Space complexity:
There is no additional data structure created so the complexity is O(1)