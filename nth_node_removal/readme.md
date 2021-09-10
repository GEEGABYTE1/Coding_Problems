# Removing the nth Node From A Linked List 
Given a linked list and it's index, remove the node located at the index given.


# Solution
This solution is inspired by the dynamic programming approach by starting from both ends of the list. We have initialized an two indicies for the start and the end. We iterate through the list checking the value of the index at the left side of the list (index at the start), and the value of the idnex at the right side of the list (index at the end of the list). If one of them matches, we can remove the value, else, we will increase the traversal from the left by adding one to the start index, and subtracting the index at the end to continue traversing the right side. 

The indicies will keep iterating until they have either crossed each other or have reached their opposite ends. Either way, the indices will not cross each other, if there is an index that is less or equal to the length of the linked list.

This dynamic programming approach divides our time complexity by a factor of 2, making our run time: `O(n/2)`, given `n` being the number of elements in a linked list. This is a minor change (two iterations instead of one) that has reduced the time by half!

Made in Python 🐍
