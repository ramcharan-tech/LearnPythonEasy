"""Frogs and Rocks

There are N rocks in a lake arranged circularly (i.e., the next rock after the last rock is the first one).
On each rock, there are some flowers (A1, A2, A3, …, AN).
A frog on the first rock can hop from one rock to another if the number of rocks between the rocks is equal to the number of flowers on the first rock.
To hop from rocks i to j, | j - i | must be equal to A[i].
The frog can hop on either side of a rock (clockwise or anticlockwise) but only chooses the side with the most flowers.
When the frog is on a certain rock, it gets flowers equal to the number of flowers on it.

Find the total number of flowers the frog gets in T hops.
 
Note
The number of flowers on a rock does not change after the frog has visited the rock.
The frog initially starts from the first rock, which has an A1 number of flowers.
The number of flowers on the rocks is distinct.
 
Function Description
In the provided code snippet, implement the provided frogAndFlowers(...) method to find the total number of flowers the frog gets in T hops. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains two integers, N and T, denoting the total number of rocks and the number of hops.
The second line contains N numbers (A1, A2, A3, …, AN) denoting the number of flowers on respective rocks.
 
Sample Input

5 3                               -- denotes N and T
3 5 2 1 4                      -- denotes N numbers

Constraints
2 <= N <= 100
1 <= T <= 100
 
Output Format
The output contains a single number denoting the total number of flowers the frog gets in T hops.
 
Sample Output
12
 
Explanation
The frog starts from the first index, which has 3 flowers.
It currently has 3 flowers.
It can perform only 3 hops.

For the first hop, it can hop over 3 rocks in either a clockwise or anticlockwise direction.
In the clockwise direction, the 3rd rock from the current one has 1 flower.
In the anticlockwise direction (3 -> 4 -> 1 -> 2), the 3rd rock has 2 flowers.
The frog selects the direction with the maximum number of flowers, chooses the anticlockwise direction (2 is greater than 1), and lands on the rock with 2 flowers.
It adds 2 to the total number of flowers and becomes 3 + 2 = 5.

The frog now must make 2 hops.
The 2nd rock in the clockwise direction has 4 flowers, while that in the anticlockwise direction has 3.
It chooses the rock with 4 flowers and hops on it.
The total flowers become 5 + 4 = 9.

Now, the frog is left with only 1 hop.
The 4th rocks on either side have 1 and 3 flowers, respectively.
The frog ends its last hop on the rock with 3 flowers, and the total becomes 9 + 3 = 12.

Hence, the output is 12."""