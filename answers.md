# CMPS 2200 Assignment 5
## Answers

**Name:**_____Sam DeMarinis____________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**


The greedy algorithm would start by choosing the coin with the largest number k such that 2^k is less than N. This process is then repeated until the chosen coins eventually add up to N. The algorithm is optimal in this case because the coins are all powers of 2.




- **1b.**

The work and span are O(logn).




- **2a.**

The counterexample is very similar to the classic knapsack problem. For example, let's say that a given bank has coin denominations of 1, 4, 6, 7, and you have 10 dollars. The greedy algorithm would select 7, then 1, then 1, and then 1. But the optimal selection for the least amount of coins is 6 and then 4. The greedy algorithm cannot work properly because the optimal selection does not always result from the largest initial choice.




- **2b.**


My algorithm would start with the highest and second highest denomination. It would create a tree where those nodes have children of the next and second next highest denominations as long as they don't exceed N. We then create a dictionary that maps each intermediate difference to the number of steps that it took to get there, where these are updated as optimal number of steps change. the algorithm will eventually return the minimum number of steps it took to reach the desired N. The work and span is O(n).