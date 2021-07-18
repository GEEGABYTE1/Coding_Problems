from random import randrange
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        
        list_counter = []
        index_counter = 0
        for ll in lists:
            list_length = self.length(ll)
            list_counter.append(list_length)
        
        if 0 in list_counter:
            
            index_of_zero = []
            for i in range(len(list_counter)):
                if list_counter[i] == 0:
                    index_of_zero.append(i)

            if len(index_of_zero) == len(lists):
                for ll in lists:
                    return ll

            new_list = []
            for idx in range(len(lists)):
                for new_idx in index_of_zero:
                    if idx == new_idx:
                        break 
                    else:
                        new_list.append(lists[idx])
                        break

            lists = new_list                            #Upadting the list
                
        if len(lists) == 0:
            for ll in lists:
                return ll
        else:
            one_big_list = []
            for linked_list in lists:
                current_node = linked_list
                while current_node:
                    if current_node.val != None:
                        one_big_list.append(current_node.val)
                    current_node = current_node.next 

            sorted_array = self.quicksort(one_big_list, 0, len(one_big_list) - 1)



            head_node = ListNode(sorted_array[0])
            sorted_ll = head_node
            #sorted_ll.next = head_node


            for num in range(len(sorted_array)):
                if num == 0:
                    pass
                else:
                    new_node = ListNode(sorted_array[num])
                    head_node.next = new_node
                    head_node = new_node


            return sorted_ll
        
                
    def quicksort(self, lst, start, end):
        if start >= end:
            return lst 
        else:
            pivot_idx = randrange(start, end)
            pivot_elm = lst[pivot_idx]
            lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]
            lesser_than_pointer = start 
            
            for i in range(start, end):
                if lst[i] < pivot_elm:
                    lst[i], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[i]
                    lesser_than_pointer += 1
            
            lst[end], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[end]
            self.quicksort(lst, start, lesser_than_pointer - 1)
            self.quicksort(lst,lesser_than_pointer + 1, end )
            
            return lst
    
    def length(self, linked_list):
        cur_node = linked_list
        counter = 0
        while cur_node:
            if cur_node.val != None:
                counter += 1
            cur_node = cur_node.next
        return counter
        