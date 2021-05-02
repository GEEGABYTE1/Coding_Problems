import random 
class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0 

    def add(self, element):
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()
    
    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return (idx * 2) + 1

    def parent_idx(self, idx):
        return idx // 2

    def heapify_up(self):
        idx = self.count 
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent > child:
                print("Swapping {parent} with {child} ".format(parent=parent, child=child))
                self.heap_list[self.parent_idx(idx)] = child 
                self.heap_list[idx] = parent 
            
            idx = self.parent_idx(idx)
        
        print("Heap Restored {} ".format(self.heap_list))

    
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            if parent > child:
                print("Swapping {parent} with {child} ".format(parent=parent, child=child))
                self.heap_list[smaller_child_idx] = parent 
                self.heap_list[idx] = child 
            
            idx = smaller_child_idx
        
        print("Heap Restored {}".format(self.heap_list))

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("Only the left child is available! ")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]

            if left_child < right_child:
                print("The left child is smaller! ")
                return self.left_child_idx(idx)
            else:
                print("The right child is smaller! ")
                return self.right_child_idx(idx)
    
    def child_present(self, idx):
        if self.left_child_idx(idx) <= self.count:
            return True 

    def retrieve_min(self):
        if self.count == 0:
            print("The Heap is empty ")
            return None 
        else:
            minimum = self.heap_list[1]
            print("Removing {min} from {heap} ".format(min=minimum, heap=self.heap_list))
            self.heap_list[1] = self.heap_list[-1]
            self.heap_list.pop()
            self.count -= 1
            self.heapify_down()
            return minimum 

    def traverse(self, num):
        checker = False
        if self.count == 0:
            print("The heap is empty! ")
            return None 
        else:
            for i in range(len(self.heap_list)):
                if self.heap_list[i] == num:
                    if self.parent_idx(i) % 2 == 0:
                        print("The value you found is a parent node! ")
                        
                    elif self.left_child_idx(i) % 2 == 0:
                        print("The value you found is a child node on the left side of the binary tree! ")
                    
                    elif self.right_child_idx(idx) % 2 == 1:
                        print("The value you found is a child node on the right side of the binary tree! ")
                    
                    print("Your value {value} ".format(value=self.heap_list[i]))
                    print("Your value was at index {index} ".format(index=i))
                    checker = True 

            if checker == False:  
                print("Your value was not found! ")
            else:
                pass
            

                    




lst = []

heap = MinHeap()
for i in range(10):
    random_number = random.randint(1, 10)
    lst.append(random_number)

for i in lst:
    heap.add(i)

print(heap.heap_list)

print(heap.traverse(5))
    