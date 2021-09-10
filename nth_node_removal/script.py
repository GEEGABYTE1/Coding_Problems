from LinkedList import BiDirectionalLinkedList

class Script:
    def script(self, ll, counter):
        front_node_counter = 1
        back_node_counter = 0
        current_node = ll.head_node
        while current_node:
            if current_node.get_value() != None:
                back_node_counter += 1
            current_node = current_node.get_link()
        current_node = ll.head_node
        end_node = ll.tail_node

        if counter > back_node_counter:
            return None

        
        while current_node and end_node:
            if front_node_counter == counter:
                node = current_node
                node_value = current_node.get_value()
                ll.remove_by_value(node_value)
                break
            else:
                current_node = current_node.get_link()
                front_node_counter += 1
            
            if back_node_counter == counter:
                node = end_node 
                node_value = end_node.get_value()
                ll.remove_by_value(node_value)
                break
            else:
                end_node = end_node.get_prev_link()
                back_node_counter -= 1
        

        print(ll.stringify_list())
        return ll


# Test Inputs 

linkedlist = BiDirectionalLinkedList()
linkedlist.add_to_head(1)
linkedlist.add_to_tail(2)
linkedlist.add_to_tail(3)
linkedlist.add_to_tail(4)
linkedlist.add_to_tail(5)

test = Script()



print(test.script(linkedlist, 3))