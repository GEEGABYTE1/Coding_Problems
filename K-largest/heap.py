class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0 

    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()

    def retrieve_min(self):
        if self.count == 0:
            print('The Heap is empty! ')
            return None 
        else:
            minimum = self.heap_list[1]
            print("Removing {min} from {heap} ".format(min=minimum, heap=self.heap_list))
            self.heap_list[1] = self.heap_list[-1]
            self.heap_list.pop()
            self.count -= 1
            self.heapify_down()
            return minimum 
    
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return (idx * 2) + 1

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print('There is only a left child! ')
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]

            if left_child < right_child:
                print("The left child is smaller than the left child ")
                return self.left_child_idx(idx)
            else:
                print("The right child is smaller than the left child")
                return self.right_child_idx(idx)
    
    def child_present(self, idx):
        if self.left_child_idx(idx) <= self.count:
            return True 
    
    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent > child:
                print("Swapping {p} with {c} ".format(p=parent, c=child))
                self.heap_list[idx] = parent 
                self.heap_list[self.parent_idx(idx)] = child 
            
            idx = self.parent_idx(idx)
        
        print("Heap Restored {} ".format(self.heap_list))
    
    def heapify_down(self):
        idx = 1 
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            if parent > child:
                self.heap_list[smaller_child_idx] = parent 
                self.heap_list[idx] = child 
            
            idx = smaller_child_idx
        
        print("Heap Restored {} ".format(self.heap_list))




class Solution:
    def firstKelements(self, arr, size, k):
        test = MinHeap()
        for i in arr:
            test.add(i)

        if len(test.heap_list) > size + 1:
            return None 
        else:
            test.heap_list = test.heap_list[:k]
        
        heap_list = test.heap_list[1:]
        print(heap_list)


solution = Solution()

lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]

solution.firstKelements(lst, len(lst), 5)