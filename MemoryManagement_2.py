
# Global constant for the list size.
LIST_SIZE = 128

# The Node class.
class Node:

    def __init__(self):

        self.process_id = None
        self.next = None
        
# Memory superclass definition.
class Memory:

    def __init__(self):

        # Memory block pointers
        self.__head = None  # Points to the first node.
        self.__current = None   # Points to the current node (used for traversing the list).
        self.__emptyBlk = None  # Points to the first node of unallocated memory.
        
	    # Memory attributes
        self.__size = 0 #  Stores the number of memory blocks.
        self.__allocations = 0  # Stores the total number of allocations.
        self.__deallocations = 0    # Stores the total number of deallocations. 
        self.__denied_allocations = 0   # Stores the number of failed allocation requests.
        self.__fragments = 0    # Stores the number of memory fragments (unallocated memory of 1 - 2 blocks in size).
        self.__node_count = 0   # Counter to help track position during list traversal (holds the number of nodes traversed).

        # Memory statistics
        self.__average_fragmentation = 0.0   # Stores the average percentage of memory fragmentation = (self.__fragments / self.__allocations)
        self.__average_allocation_time = 0.0  # Stores the average time it takes to allocate memory space for a process = (count / self.__allocations)
        self.__percentage_denied = 0.0    # Percentage of failed allocation requests = (self.__denied_allocations / self.__allocations)
        
        # Initiates the head node for the memory linked list.
        block = Node()
        self.__head = self.__current = self.__emptyBlk = block
        block.process_id = -1
        block.next = None
        self.__size = 1
        

        # Loop for adding the rest of the nodes.

        for i in range(0, (LIST_SIZE - 1)):
            block = Node()
            block.process_id = -1
            block.next = None
            self.__current.next = block
            self.__current = block
            self.__size += 1
        self.__current = self.__head

    # Accessor method for total number of allocations.
    def get_allocations(self):

        return self.__allocations

    # Accessor method for total number of deallocations.
    def get_deallocations(self):

        return self.__deallocations

    # Accessor method for total number of denied allocations.
    def get_denied_allocations(self):

        return self.__denied_allocations

    # Method which will count and return the total number of memory fragments.
    def get_fragments(self):

        frags = 0
        count = 0
        self.__current = self.__head
        while self.__current != None:
            count = 0
            if self.__current.process_id == -1:
                while self.__current != None and self.__current.process_id == -1:
                    count += 1
                    self.__current = self.__current.next
                if count > 0 and count < 3:
                    frags += 1
                if self.__current == None:
                    self.__fragments += frags
                    return self.__fragments
            self.__current = self.__current.next
        self.__fragments += frags
        return self.__fragments

    # Method which will calculate and return the average memory fragmentation.
    def get_average_fragmentation(self):

        self.__average_fragmentation = (format(self.__fragments / self.__allocations, '.4f'))
        return self.__average_fragmentation

    # Method which will calculate and return the average time it takes to allocate memory to processes.
    def get_average_allocation_time(self):

        self.__average_allocation_time = (format(self.__node_count / (self.__allocations - self.__denied_allocations), '.4f'))
        return self.__average_allocation_time

    # Method which will calculate and return the percentage of denied allocations.
    def get_percentage_denied(self):

        self.__percentage_denied = (format(self.__denied_allocations / self.__allocations, '.0%'))
        return self.__percentage_denied

    # Test method used to access the data in the head node only.
    def get_head_pointer(self):

        return self.__head.process_id

    # Generic memory allocation method (gets an override in each of the 4 algorithms).
    def allocate_memory(self, process_id, num_units):

        return -1

    # Generic memory deallocation method (same method for all 4 algorithms).
    def deallocate_memory(self, process_id):

        self.__current = self.__head
        self.__deallocations += 1
        while self.__current != None and self.__current.process_id != process_id:
            self.__current = self.__current.next
        if self.__current == None:
            self.__current = self.__head
            return -1
        while self.__current != None and self.__current.process_id == process_id:
            self.__current.process_id = -1
            self.__current = self.__current.next
        self.__current = self.__head
        return 1

    # Generic print memory list method (same method for all 4 algorithms).
    def print(self):

        count = 0
        current_node = self.__head
        while current_node != None:
            print(count, '->', current_node.process_id, '\n')
            count += 1
            current_node = current_node.next
        print()
        print('Number of 2KB blocks:', self.__size)
        print()
        print('Total memory capacity: ', (self.__size * 2), 'KB', sep='')
        print('\n\n')

# First fit subclass definition.
class First_Fit(Memory):

    def allocate_memory(self, process_id, num_units):
        
        allocation_size = 0
        node_count_local = 1
        self._Memory__allocations += 1
        self._Memory__current = self._Memory__head
        if num_units < 3 or num_units > 10:
            return -1
        for i in range(0, (LIST_SIZE - 1)):
            allocation_size = 0
            if self._Memory__current == None:
                self._Memory__denied_allocations += 1
                return -1
            if self._Memory__current.process_id == -1:
                self._Memory__emptyBlk = self._Memory__current
                while self._Memory__current != None and self._Memory__current.process_id == -1 and allocation_size < num_units:
                    allocation_size += 1
                    self._Memory__current = self._Memory__current.next
                    node_count_local += 1
                if allocation_size == num_units:
                    self._Memory__current = self._Memory__emptyBlk
                    while allocation_size != 0:
                        self._Memory__current.process_id = process_id
                        self._Memory__current = self._Memory__current.next
                        allocation_size -= 1
                    self._Memory__node_count = node_count_local
                    return self._Memory__node_count
                if self._Memory__current == None:
                    self._Memory__denied_allocations += 1
                    return -1
            self._Memory__current = self._Memory__current.next
            node_count_local += 1

# Best fit subclass definition.
class Best_Fit(Memory):

    def allocate_memory(self, process_id, num_units):

        allocation_size = 0
        node_count_local = 1
        best_size = 128
        current_adequate = False
        adequate = False
        self._Memory__allocations += 1
        self._Memory__current = self._Memory__head
        next_node = self._Memory__current
        best_node = None

        if num_units < 3 or num_units > 10:
            return -1
        while self._Memory__current.next != None:
            self._Memory__current = next_node
            current_adequate = False
            if self._Memory__current.process_id == -1:
                self._Memory__emptyBlk = self._Memory__current
                allocation_size = 0
                while self._Memory__current.process_id == -1:
                    allocation_size += 1
                    if allocation_size >= num_units:
                        current_adequate = True
                        adequate = True
                    if self._Memory__current.next != None and self._Memory__current.next.process_id != -1:
                        next_node = self._Memory__current.next
                        node_count_local += 1
                        break
                    elif self._Memory__current.next != None:
                        self._Memory__current = self._Memory__current.next
                        node_count_local += 1
                    else:
                        break
                if current_adequate and (allocation_size < best_size):
                    best_size = allocation_size
                    best_node = self._Memory__emptyBlk
            elif self._Memory__current.next != None:
                self._Memory__current = self._Memory__current.next
                next_node = self._Memory__current
                node_count_local += 1
            else:
                break
        if adequate:
            self._Memory__current = best_node
            for i in range(0, num_units):
                self._Memory__current.process_id = process_id
                if self._Memory__current.next != None:
                    self._Memory__current = self._Memory__current.next
            self._Memory__node_count += node_count_local
            return self._Memory__node_count
        else:
            self._Memory__denied_allocations += 1
            return -1
        return -1

# Next fit subclass definition.
class Next_Fit(Memory):

    def allocate_memory(self, process_id, num_units):

        

        return super().allocate_memory(process_id, num_units)

# Worst fit subclass definition.
class Worst_Fit(Memory):

    def allocate_memory(self, process_id, num_units):



        return super().allocate_memory(process_id, num_units)

# Test method used during linked list implementation.
#def main():

    #ff_memory = First_Fit()
    #ff_memory.print()
    #ff_memory.allocate_memory(7, 3)

    #frags = memory.get_fragments
    #print(frags)
    #memory.print()

    #dealloc = memory.deallocate_memory("I'm the head node!")
    #print()
    #memory.print()

    #num = memory.get_head_pointer()
    #print(num)
    
#main()
