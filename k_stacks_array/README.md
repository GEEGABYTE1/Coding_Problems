# Implement K stacks in a single array 

Problem: Create a data structure that represents k stacks. The data structure must allow each k stack to add, pop, and print node(s).

# Solution 

We used a data structure for the backend, which had the push and pop functions. 

The push function will set the new node's link to the top item and will set that as the top item.

The pop function will set the top item as the item to remove. The new top item will be set as the current top item's (item to remove) link.

The print function is a combination of both. Since the stack does not allow traversal, we keep popping and print the popped node from the desired stack. We also add this node to a list to keep track of the nodes that were removed, in order to add them back to the stack so the stack remains "unaffected". 


# More Information 

Push Function: `O(1)` (both from the `Stack()` and `K_Stack()`)
Pop Function: `O(1)` (both from the `Stack()` and `K_Stack()`)
Print Function: `O(n^2)` (from the `K_Stack()`)

Made in Python 🐍
Problem from: https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/