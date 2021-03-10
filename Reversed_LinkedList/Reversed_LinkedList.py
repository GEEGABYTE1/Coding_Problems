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

    def updated_value(self, new_value):
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
        string_lst = ""
        current_node = self.get_head_node() 
        while current_node:
            if current_node.get_value() != None:
                string_lst += str(current_node.get_value()) + "\t"
                print(string_lst)
                string_lst = ""
            current_node = current_node.get_link()
        

    def remove_node(self, item_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == item_to_remove:
            self.head_node = current_node.get_link()
        else:
            while current_node:
                next_node = current_node.get_link()                                 ###Iteration only works under the while loop####
                if next_node.get_value() == item_to_remove:
                    current_node.set_link(next_node.get_link())
                    current_node = None 
                else:
                    current_node = next_node                                        ### Part of Iteration ###
    
    
    def reverse_list(self):
        current_node = self.get_head_node()
        current_node2 = self.get_head_node()
        base_node = self.get_head_node()
        

        while current_node.get_value() != None:
            next_node = current_node.get_link()
            try:
                if next_node.get_link() == None:
                    print(next_node.get_value())
                    current_node.set_link(None)
                    next_node.set_link(current_node)
                    next_node = current_node2
                    
                current_node = next_node
            except AttributeError:
                print(base_node.get_value())
                break

        

#### Test inputs####            

ll = LinkedList(1)
ll.insert_node(2)
ll.insert_node(3)
ll.insert_node(4)
ll.insert_node(5)
ll.insert_node(6)

#print(ll.reverse_list())
#print(ll.stringify_list())
