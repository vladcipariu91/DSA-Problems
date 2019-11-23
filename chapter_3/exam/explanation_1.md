## Time complexity:
To solve this problem I used Newton's formula for calculating
the square root.
We take a guess by dividing the number.
Then we assign this guess to a temporary variable and guess
again.
We repeat this until the guess and the temporary variable are equal.
Since every time we narrow down the search interval by half the
complexity is O(log(n))


## Space complexity:
To solve the problem only two variables are needed
so the space complexity is O(1)