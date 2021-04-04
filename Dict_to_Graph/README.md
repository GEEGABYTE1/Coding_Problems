
# Problem

Given a dictionary, implement a graph. The keys of the dictionary used are the nodes of our graph and the corresponding values are lists with each nodes, which are connecting by an edge. 
This simple graph has six nodes (a-f) and five arcs: 

- `a -> c `
- `b -> c `
- `b -> e `
- `c -> a `
- `c -> b `
- `c -> d `
- `c -> e `
- `d -> c `
- `e -> c `
- `e -> b `

## Input  
`graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        } `
        
## Output 

`[('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'a'), ('c', 'b'), 
('b', 'c'), ('b', 'e'), ('e', 'b'), ('e', 'c'), ('d', 'c')]`

  ### Graphic Illustration 
  <img src=https://media.geeksforgeeks.org/wp-content/uploads/python1.jpg>

# Extras:
Solution to full problem coming soon! 

Made in Python 🐍


# Refernence:

GeeksforGeeks 
Link to problem: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
