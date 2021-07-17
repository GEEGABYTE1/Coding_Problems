from script import test

# Test Cases

# Test Case 1

print(test.isMatch('aa', 'a'))              # False

# Test Case 2

print(test.isMatch('aa', 'a*'))             # True

# Test Case 3

print(test.isMatch('ab', '.*'))             # True

# Test Case 4 

print(test.isMatch('aab', 'c*a*b'))         # True

# Test Case 5 

print(test.isMatch('mississippi', 'mis*is*p*'))     # False


# All solutions annotated are from LeetCode