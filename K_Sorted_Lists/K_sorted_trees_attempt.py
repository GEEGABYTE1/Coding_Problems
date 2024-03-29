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
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print(current_node.get_value())
            current_node = current_node.get_link()
    
    def remove(self, value):
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


class Solution:
    
    def k_sorted(self, lst):
        merged_lst = LinkedList()
        for i in lst:
            current_node = i.get_head_node()
            while current_node:
                if merged_lst.get_head_node().get_value() == None:
                    merged_lst = LinkedList(current_node.get_value())
                else:
                    if current_node.get_value() != None:
                        merged_lst.insert_node(current_node.get_value())
                current_node = current_node.get_link()
        
        return self.bubble_sort(merged_lst)

            

    def bubble_sort(self, lst):
        values = []
        current_node = lst.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                values.append(current_node.get_value())
            current_node = current_node.get_link()

        max_value = max(values)
        max_exponent = len(str(max_value))
        being_sorted = values[:]

        for exponent in range(max_exponent):
            position = exponent + 1
            index = -position 
            digits = [ [] for i in range(10)]

            for number in being_sorted:
                string_number = str(number)
                try:
                    digit = string_number[index]
                except IndexError:
                    digit = 0 
                
                digit = int(digit)
                digits[digit].append(number)
                being_sorted = []
                for numeral in digits:
                    being_sorted.extend(numeral)

                #print(values)

        lst = LinkedList(being_sorted[0])
        for i in range(len(being_sorted)):
            if i == 0:
                pass
            else:
                lst.insert_node(being_sorted[i])
        
        return lst.stringify_list()

            
        
        

lst = LinkedList()

lst.insert_node(5)
lst.insert_node(4)
lst.insert_node(1)
lst.insert_node(9)


lst2 = LinkedList()

lst2.insert_node(1)
lst2.insert_node(3)
lst2.insert_node(1)

test = Solution()

test.k_sorted([lst, lst2])
