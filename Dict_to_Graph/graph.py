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
        self.graph = Graph()
        for i, j in dictionary.items(): 
            current_new_vertex = Vertex(i)
            self.graph.add_vertex(current_new_vertex)
            
            for k in j:
                current_new_edge = Vertex(k)
                if current_new_edge.value in list(self.graph.graph_dict.keys()):
                    pass
                else:
                    self.graph.add_vertex(current_new_edge)
                self.graph.add_edge(current_new_vertex, current_new_edge)


        lst = []
        for i, j in self.graph.graph_dict.items():
            
            for k in j.get_edges():
                test = (i, k)
                lst.append(test)
        
        print(lst)

    def path(self, dictionary, start, end):
        lst = []
        values_to_go_to = []
        
        for i, j in self.graph.graph_dict.items():
            values = []
            if not i in lst:
                lst.append(i)
            
            for k in j.get_edges():
                values.append(k)

            if end in values:
                lst.append(end)
                
            else:
                for s in self.graph.graph_dict.keys():
                    values_to_go_to.append(lst)
                for l in range(len(j.get_edges()), 0, -1):
                    values_to_go_to.append(j.get_edges[l])
                    #if not l in lst:
                        #lst.append(l)
                i = values_to_go_to.pop()

   
    def generate_path(self, dictionary, from_key, to_key):
        lst = []
        lst.append(from_key)
        for i, j in self.graph.graph_dict.items():
            if not to_key in j.get_edges():
                continue 
            else:
                self.graph.add_edge(Vertex(i), Vertex(to_key))
                lst.append(i)
                lst.append(to_key)
                break 
        print(lst)
        
        lst = []
        values_to_go_to = []
        for i, j in self.graph.graph_dict.items():
            values = []
            if not i == from_key:
                pass 
            else:
                if not i in lst:
                    lst.append(i)
                
                for k in j.get_edges():
                    values.append(k)
                
                if to_key in values:
                    lst.append(end)
                
                else:
                    for s in self.graph.graph_dict.keys():
                        values_to_go_to.append(lst)
                    for l in range(len(j.get_edges()), 0, -1):
                        values_to_go_to.append(j.get_edges[l])
                    
                    i = values_to_go_to.pop()
                
    
    def real_gen_path(self, dictionary, from_key, to_key):
        lst = []
        lst.append(from_key)
        values = []
        #for l in range(len(l.get_edges()), 0, -1):
            #values_to_go_to.append(l.get_edges[l])

        for i in self.graph.graph_dict.keys():
            if len(values) == 0:
                i = from_key 
            if len(values) > 1:
                i = values.pop()
            #if self.graph.graph_dict[i] == self.graph.graph_dict[from_key]:
                
            right_vertex = self.graph.graph_dict[i]
            
            if not to_key in right_vertex.get_edges():
                
                for k in range(len(right_vertex.get_edges()), 0, -1):
                    values.append(right_vertex.get_edges()[k - 1])
                
                
            else:
                self.graph.add_edge(Vertex(from_key), Vertex(right_vertex.value))
                self.graph.add_edge(Vertex(right_vertex.value), Vertex(to_key))
                if not self.graph.graph_dict[i] in lst:
                    lst.append(i)
                lst.append(to_key)
                print(lst)
                break
        
        return lst

    
                    


        

        
            
        
        
        

            




            





dictionary_test = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

dictionary_test2 = {
    'a': ['c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a', 'd'],
    'e': ['b', 'c']
}


#test = Prompt({ "a" : ["c"],
          #"b" : ["c", "e"],
          #"c" : ["a", "b", "d", "e"],
         # "d" : ["c"],
         # "e" : ["c", "b"],
         # "f" : []
        #})


test2 = Prompt(dictionary_test2)
test2.real_gen_path(dictionary_test2, 'd', 'c')
