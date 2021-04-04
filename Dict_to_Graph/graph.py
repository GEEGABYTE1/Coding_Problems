class Vertex:
    def __init__(self, value):
        self.value = value 
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight 

    def get_edges(self):
        return list(self.edges.keys())


class Graph:
    def __init__(self, directed=False):
        self.directed = directed 
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print('Adding {}'.format(vertex.value))
        self.graph_dict[vertex.value] = vertex 

    def add_edge(self, from_vertex, to_vertex):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)

        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop()
            seen[current_vertex] = True 
            print(current_vertex)

            if current_vertex == end_vertex:
                return True 
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [i for i in next_vertices if not i in seen]

                start.extend(next_vertices)
            
        return False



class Prompt:
    def __init__(self, dictionary):
        graph = Graph()
        for i, j in dictionary.items(): 
            current_new_vertex = Vertex(i)
            graph.add_vertex(current_new_vertex)
            
            for k in j:
                current_new_edge = Vertex(k)
                graph.add_vertex(current_new_edge)
                graph.add_edge(current_new_vertex, current_new_edge)


        ### Testing inputs ###
        print(graph.graph_dict)
        for i, j in graph.graph_dict.items():
            print('{key} edges: {edges} '.format(key=i, edges=j.get_edges()))




            








test = Prompt({ "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }) 

