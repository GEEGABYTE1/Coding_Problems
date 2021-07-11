from vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex 
    
    def add_edge(self,from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)

        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
    
    def traverse(self, start_vertex, end_vertex):
        start = [start_vertex]
        nodes = []
        seen = {}
        while len(start) > 0:
            nodes.append(start[0])
            current_vertex = start.pop()
            seen[current_vertex] = True 
            if current_vertex == end_vertex:
                nodes.append(current_vertex)
                break
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [i for i in next_vertices if not i in seen]
                start.extend(next_vertices)
            
        return nodes


    def single_direct(self):
        nodes = {}
        for i, j in self.graph_dict.items():
            edges = list(j.edges.keys())
            nodes[i] = edges
        
        return nodes

    def path_visualizer(self, nodes, path=[], counter=0, root_element=None):

        if counter == len(list(nodes.keys())):
            return None
        
        elif len(list(nodes.keys())) == 1:
            return nodes
            
        else:
            element = list(nodes.keys())[counter]
            for i in nodes[element]:
                path.append(i)
                if root_element in nodes[i]:
                    #path.append(i)
                    path.append(root_element)
                    if path[0] != root_element:
                        path = [root_element] + path
                else:
                    for index in range(len(list(nodes.keys()))):
                        if list(nodes.keys())[index] == i:
                            

                            root_node_occurances = []
                            for j in self.graph_dict.values():
                                for edge in j.edges.keys():
                                    root_node_occurances.append(edge)
                            
                            root_node_occurances = sorted(root_node_occurances)
                            root_node_occurances_counter = 0                                # Linear Search
                            for node in root_node_occurances:
                                if node == root_element:
                                    root_node_occurances_counter += 1
                                    break 
                            
                            if root_node_occurances_counter > 0:
                                counter = index 
                                return self.path_visualizer(nodes, path, counter, root_element)
                            else:
                                counter += 1
                                return self.path_visualizer(nodes, path, counter, root_element=list(nodes.keys())[counter])

            if len(path) == 0:
                pass
            elif path[0] == path[-1] and len(path) != 1:
                return path 
        
            counter += 1
            #path.append(element)
            return self.path_visualizer(nodes, path, counter, root_element=list(nodes.keys())[counter])





## Test ##
zero = Vertex(0)
one = Vertex(1)
two = Vertex(2)
three = Vertex(3)

test = Graph(directed=True)
test.add_vertex(zero)
test.add_vertex(one)
test.add_vertex(two)
test.add_vertex(three)


# Pass case #
'''test.add_edge(zero, one)
test.add_edge(zero, two)
test.add_edge(one, two)
test.add_edge(two, three)
test.add_edge(three, one)'''


# Pass case #
'''test.add_edge(zero, one)
test.add_edge(one, three)
test.add_edge(three, two)
test.add_edge(two, zero)'''




nodes = test.single_direct()

print(test.path_visualizer(nodes, root_element=list(nodes.keys())[0]))
