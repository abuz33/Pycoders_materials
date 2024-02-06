# Class4-CS101Module-Week10


## Question 1:

Given n ropes of different lengths, connect them into a single rope with minimum cost. Assume that the cost to connect two ropes is the same as the sum of their lengths.(Hint: Use a priority queue implemented using min-heap)

**Input:**

`[5,4,2,8]` 

**Output :** 

`The minimum cost is 36`

```
For example,

[5, 4, 2, 8] –> First, connect ropes of lengths 4 and 2 that will cost 6.
[5, 6, 8]    –> Next, connect ropes of lengths 5 and 6 that will cost 11.
[11, 8]      –> Finally, connect the remaining two ropes that will cost 19.
Therefore, the total cost for connecting all ropes is 6 + 11 + 19 = 36.
```



## Question 2:

Given a binary array, sort it in linear time and constant space by modifying the partitioning logic of the Quicksort algorithm. The output should print all zeroes, followed by all ones.
For example,

**Input:**

`{1,0,1,0,1,0,0,1}` 

**Output :** 

`{0,0,0,0,1,1,1,1}` 


## Question 3:

Construct a following tree.
```
              1
            /   \
           /     \
          2       3
         /      /  \
        /      /    \
       4      5      6
             / \
            /   \
           7     8
```
Take this binary tree, calculate the difference between the sum of all nodes present at odd levels and the sum of all nodes present at even level.
You should get the required difference as output is:

`(1+4+5+6) - (2+3+7+8) = -4` 



