
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    
    def traverse(self):
        self.root_node = self.value 
        self.root_node_children = self.children
        level = 1
        node = self
        while len(node.children) > 0:
            node.value = node.children[0].value
            node.children = node.children[0].children  
            level += 1
        node.value = self.root_node
        node.children = self.root_node_children 
        return level

    def print_values(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.value)
            nodes += current_node.children 
    
# Initialize Trees #

#Test Cases #


tree = TreeNode('A')
tree2 = TreeNode('B')
tree3 = TreeNode('C')

tree.add_child(tree2)
tree2.add_child(tree3)

#tree.traverse()
            
second_tree_zero = TreeNode(5)
second_tree  = TreeNode(1)
second_tree2 = TreeNode(2)
second_tree3 = TreeNode(3)
second_tree4 = TreeNode(4)

second_tree_zero.add_child(second_tree)


tree.traverse()

#second_tree.traverse()



# Solution

def comparision_tree(tree1, tree2):
    tree1_level = tree1.traverse()
    tree2_level = tree2.traverse()

    if tree1_level < tree2_level:
        tree1.print_values()
    elif tree2_level < tree1_level:
        tree2.print_values()
    else:
        return 0 


print(comparision_tree(tree, second_tree_zero))
    

