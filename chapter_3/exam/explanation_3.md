## Time complexity:
To solve this problem I used merge sort. The complexity of merge sort is O(n log(n)).
On top of this I need to iterate over the sorted array and pick the numbers. For the first number
I pick the even indices of the array and for the second number I pick the odd ones.
To create the numbers the time complexity is O(n).
The resulting complexity of this solution is O(n + n log(n)) hence the resulting complexity is
O(n log(n)).

## Space complexity:
To solve this problem I used merge sort. Since merge sort creates a new list to store the sorted
elements the space complexity of this problem is O(n).