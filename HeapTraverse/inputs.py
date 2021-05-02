from heaps import MinHeap 
from heaps import random

lst = []

heap = MinHeap()
for i in range(10):
    random_number = random.randint(1, 10)
    lst.append(random_number)

for i in lst:
    heap.add(i)

print(heap.heap_list)

print(heap.traverse(5))
    