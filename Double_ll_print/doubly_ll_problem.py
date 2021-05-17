class Node:
    def __init__(self, value, link=None, prev_link=None):
        self.value = value 
        self.link = link 
        self.prev_link = prev_link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 

    def set_prev_link(self, new_link):
        self.prev_link = new_link 

    def get_prev_link(self):
        return self.prev_link 


class DoubleLinkedList:
    def __init__(self):
        self.head_node = None 
        self.tail_node = None 

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node 

        if current_head != None:
            current_head.set_prev_link(new_head)
            new_head.set_link(current_head)
        
        self.head_node = new_head 

        if self.tail_node == None:
            self.tail_node = new_head 
        
    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node 

        if current_tail != None:
            current_tail.set_link(new_tail)
            new_tail.set_prev_link(current_tail)
        
        self.tail_node = new_tail 

        if self.head_node == None:
            self.head_node = new_tail 
    
    def remove_head(self):
        removed_head = self.head_node 
        if removed_head == None:
            return None 
        else:
            self.head_node = removed_head.get_link()
            
            if self.head_node != None:
                self.head_node.set_prev_link(None)
            else:
                if removed_head == self.tail_node:
                    self.remove_tail()
        
        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node 
        if removed_tail == None:
            return None 
        else:
            self.tail_node = removed_tail.get_prev_link()

            if self.tail_node != None:
                self.tail_node.set_link(None)
            else:
                if removed_tail == self.head_node:
                    self.remove_head()
        
        return removed_tail 

    def get_head_node(self):
        return self.head_node

    def stringify_list(self):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print(current_node.get_value())
            
            current_node = current_node.get_link()





test = DoubleLinkedList()

def split_list(lst):
    
    middle = len(lst) // 2
    left_split = lst[:middle]
    right_split = lst[middle:]

    for i in left_split:
        test.add_to_head(i)
    
    for i in right_split:
        test.add_to_tail(i)
    
    test.stringify_list()
    print()

    for i in range(len(lst)):
        if i % 2 == 0:
            test.remove_head()
            test.stringify_list()
            print()
        else:
            
            test.remove_tail()
            test.stringify_list()
            print()
        

lst = [0, 1, 2, 3, 4]



print(split_list((lst)))