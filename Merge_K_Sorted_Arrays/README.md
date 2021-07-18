# Problem 

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

*From LeetCode*

## Example 1

- `Input: lists = [[1,4,5],[1,3,4],[2,6]]`
- `Output: [1,1,2,3,4,4,5,6]`
- `Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6`

## Example 2
- `Input: lists = []`
- `Output: []`

## Example 3:
- `Input: lists = [[]]`
- `Output: []`

## Example 4:
- `Input: lists =[[]. [1]]`
- `Output: [1]`

## Example 5:
- `Input: lists = [[],[-1,5,11],[],[6,10]]`
- `Output: [-1,5,6,10,11]`

# Solution 

There wasn't any nitty-gritty things in the solution. Rather, my solution is long rather than complex making it very intuitive. The only thing you can consider when it comes to technicalities is my insertion of the *quicksort* algorithm. That was needed to sort all the values of each Linked List.

# More Information 
 
Original Problem: https://leetcode.com/problems/merge-k-sorted-lists/

Made in Python 🐍
