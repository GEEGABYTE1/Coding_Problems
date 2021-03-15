class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    
    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [i for i in self.children if i != child_node]

    def reverse(self):
        node = [self]

        while len(node) > 0:
            current_node = node.pop()
            print(current_node.value)
            if len(current_node.children) > 0:
                right_side = current_node.children[-1]
                left_side = current_node.children[0]

                current_node.children = [right_side, left_side]
            else:
                pass
            node += current_node.children
    
    def traverse(self):
        nodes_to_visit = [self]

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children
            
        
        


            

            
            
            

        
test = TreeNode(1)
test2 = TreeNode(2)
test3 = TreeNode(3)
test4 = TreeNode(4)
test5 = TreeNode(5)
test6 = TreeNode(6)
test7 = TreeNode(7)

test.add_child(test2)
test.add_child(test3)
test2.add_child(test4)
test2.add_child(test5)
test3.add_child(test6)
test3.add_child(test7)
print(test.traverse())
print(test.reverse())

