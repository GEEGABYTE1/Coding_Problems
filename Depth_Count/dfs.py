from Tree import Tree

def dfs(root_node, goal, path=(), count=-1):
    path = path + (root_node,)

    count += 1
    if root_node.value == goal:
        pass
    else:
        for child in root_node.children:
            new_path = dfs(child, goal, path, count)

            if new_path != None:
                return new_path 
        

    return count





