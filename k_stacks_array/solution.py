from Stack import Stack 

class K_Stack:

    def __init__(self, stack_num):
        self.stacks = [Stack() for i in range(stack_num)]

    def push(self, value=None, stack=None, array_size=10):

        try:
            if stack and value:
                current_stack = self.stacks[stack]
                current_stack.limit = array_size 
                current_stack.push(value)
                array_size -= 1
            else:
                print("You have not entered a correct input")
                return 
        except IndexError:
            return 

    
    def k_stack_pop(self, stack_num):
        current_stack = self.stacks[stack_num]
        result = current_stack.pop()
        print(result.get_value())

    def printstack(self, stack_num):
        current_stack = self.stacks[stack_num]
        stack_elms = []
        while current_stack.size != 0:
            current_node = current_stack.pop()
            print(current_node.get_value())
            stack_elms.append(current_node)
        
        for i in stack_elms:
            current_stack.push(i)


# Test inputs

kstacks = K_Stack(3)

kstacks.push(15, 2)
kstacks.push(45, 2)

kstacks.push(17, 1)
kstacks.push(49, 1)
kstacks.push(39, 1)

#kstacks.k_stack_pop(2)
#kstacks.k_stack_pop(1)


kstacks.printstack(1)
