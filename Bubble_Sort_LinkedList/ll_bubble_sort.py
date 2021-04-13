class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 

    def set_value(self, new_value):
        self.value = new_value


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node 

    def insert_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_link(self.head_node)
        self.head_node = new_node 

    def stringify_list(self):
        self.counter = 0
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print(current_node.get_value())
                self.counter += 1
            
            current_node = current_node.get_link()
    
    def remove_node(self, value):
        current_node = self.get_head_node()
        if current_node.get_value() == value:
            self.head_node = current_node.get_link()
        else:
            while current_node:
                next_node = current_node.get_link()
                if next_node.get_value() == value:
                    current_node.set_link(next_node.get_link())
                    current_node = None 
                else:
                    current_node = next_node 
    

    def bubble_sort(self):
        current_node = self.get_head_node()
        next_node = current_node.get_link()
        self.count = 0
        while self.count != (self.counter*self.counter):
            if next_node.get_value() == None:
                current_node = self.get_head_node()
                next_node = current_node.get_link()
            base_current_node = current_node
            base_next_node = next_node
            if current_node.get_value() != None:
                while current_node.get_link().get_value() != None:
                    if current_node.get_value() > next_node.get_value():
                        ####
                        base_current_node = Node(current_node.get_value(), current_node.get_link())
                        base_next_node = Node(next_node.get_value(), next_node.get_link())
                        ####
                        temp = current_node.get_value()
                        current_node.set_value(next_node.get_value())
                        next_node.set_value(temp)
                    current_node = base_current_node.get_link()
                    next_node = base_next_node.get_link()
                    self.count += 1
                    
                    break

                
        self.stringify_list()


test = LinkedList()
test.insert_node(1)
test.insert_node(2)
test.insert_node(3)
test.insert_node(4)
test.insert_node(5)
print(test.stringify_list())

print(test.bubble_sort())
