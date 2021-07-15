from Tree import Tree
from dfs import dfs

tree = Tree(1)
tree2 = Tree(2)
tree3 = Tree(3)
tree4 = Tree(4)
tree5 = Tree(5)

tree.add_child(tree2)
tree2.add_child(tree3)
tree3.add_child(tree4)
tree4.add_child(tree5)
tree4.add_child(tree2)
tree.add_child(tree5)

output = dfs(tree, 4)
print(output)