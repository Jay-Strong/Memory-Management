import random, MemoryManagement_2

def generator(ff_mem, bf_mem, nf_mem, wf_mem, num_requests):

    #ff_mem = ff_memory
    #ff_mem = MemoryManagement_2.First_Fit()
    bf_mem = MemoryManagement_2.Best_Fit()
    place_holder = 0
    allocation_tester = 0
    deallocation_index = 0
    deallocation_pid = 0
    random_num = 0
    ff_list = []
    bf_list = []
    for index in range(0, num_requests):
        place_holder = ((random.randint(0, index)) % 3)
        #place_holder = (random.randint(0, index))
        # Allocation loops
        if place_holder != 0:
            random_num = (((random.randint(0, index)) % 7) + 3)
            #random_num = (random.randint(0, index))

            # First fit loop
            allocation_tester = (ff_mem.allocate_memory(index, random_num))
            if allocation_tester != -1:
                ff_list.append(index)
                ff_mem.get_fragments

            # Best fit loop
            allocation_tester = (bf_mem.allocate_memory(index, random_num))
            if allocation_tester != -1:
                bf_list.append(index)
                bf_mem.get_fragments

            # Next fit loop
            allocation_tester = (nf_mem.allocate_memory(index, random_num))
            if allocation_tester != -1:
                nf_list.append(index)
                nf_mem.get_fragments

            # Worst fit loop
            allocation_tester = (wf_mem.allocate_memory(index, random_num))
            if allocation_tester != -1:
                wf_list.append(index)
                wf_mem.get_fragments

        # Deallocation loops
        else:
           if index > 0:
                # First fit loop
                if (len(ff_list)) != 0:
                    deallocation_index = ((random.randint(0, index) % (len(ff_list))))
                    deallocation_pid = ff_list[deallocation_index]
                    del ff_list[deallocation_index]
                    ff_mem.deallocate_memory(deallocation_pid)

                # Best fit loop
                if (len(bf_list)) != 0:
                    deallocation_index = ((random.randint(0, index) % (len(bf_list))))
                    deallocation_pid = bf_list[deallocation_index]
                    del bf_list[deallocation_index]
                    bf_mem.deallocate_memory(deallocation_pid)

                # Next fit loop
                if (len(nf_list)) != 0:
                    deallocation_index = ((random.randint(0, index) % (len(nf_list))))
                    deallocation_pid = nf_list[deallocation_index]
                    del nf_list[deallocation_index]
                    nf_mem.deallocate_memory(deallocation_pid)

                # Worst fit loop
                if (len(wf_list)) != 0:
                    deallocation_index = ((random.randint(0, index) % (len(wf_list))))
                    deallocation_pid = wf_list[deallocation_index]
                    del wf_list[deallocation_index]
                    wf_mem.deallocate_memory(deallocation_pid)
