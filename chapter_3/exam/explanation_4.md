## Time complexity:
We traverse the array once and count the zeroes, the ones, the twos.
After doing this we'll replace the first elements with the number of zeroes we
collected. Then do the same for the ones and then for the twos.
The complexity is O(zeros + ones + twos + n) = O(n).

## Space complexity:
There is no additional data structure created so the complexity is O(1). The sorting
is done in place.