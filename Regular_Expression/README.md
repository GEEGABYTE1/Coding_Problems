# Regular Expression Matching 

# Problem 

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:

    - `.` Matches any single character.
    - `*` Matches zero or more of the preceding element

The matching should cover the entire input string (not partial)

# Solution 

We start off by splitting both `s` and `p` as separate lists for reference when iterating `p`. We will work backwards as it's easier to create cases based of of `.` and `*` to letters compared to vice versa.

There are multiple cases that have been taken into consideration:

    - Case 1) If p is less than s than return `False` 
    - Case 2) If the Index is 0 and both the first letters of `p` and `s` are the same, we add `p[i]` to a new string called `new_string` in our case.
    - Case 3) If `p[i]` is not in `s` and `p[i]` is neither a `*` or `.`, we then add both `*` and `p[i]` to `new_string`.
    - Case 4) If `p[i]` is in `s` and `p[i]` is neither a `*` or `.`, if `p[i]` occurs more than once simultaneously, we will add both `*` and `p[i]`, else, we will just add `p[i]`
    - Case 5) If `p[i]` == `*`, we add `*` to `new_string`/
    - Case 6) If `p[i]` == `.`, we add `.` to new_string


After the iteration is done, we then check if `new_string` is the same as `p`, if so, we return `True`, else, `False`.

Time Complexity: `O(n)` 

# More Information

Made in Python 🐍

Original Problem: https://leetcode.com/problems/regular-expression-matching/ 