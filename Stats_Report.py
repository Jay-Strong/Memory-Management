import MemoryManagement_2

def display_first_fit(ff_mem):

    #ff_mem = ff_memory
    #ff_mem = MemoryManagement_2.First_Fit()
    print()
    print("Total fragments:", ff_mem.get_fragments(), "\n")
    print("Average fragmentations:", ff_mem.get_average_fragmentation(), "\n")
    print("Average allocation time:", ff_mem.get_average_allocation_time(), "\n")
    print("Allocation request denial percentage:", ff_mem.get_percentage_denied(), "\n")
    print("Total allocation requests:", ff_mem.get_allocations(), "\n")
    print("Total allocation request denials", ff_mem.get_denied_allocations(), "\n")
    print("Total deallocations:", ff_mem.get_deallocations(), "\n")

def display_best_fit(bf_mem):

    #bf_mem = bf_memory
    #bf_mem = MemoryManagement_2.Best_Fit()
    print()
    print("Total fragments:", bf_mem.get_fragments(), "\n")
    print("Average fragmentations:", bf_mem.get_average_fragmentation(), "\n")
    print("Average allocation time:", bf_mem.get_average_allocation_time(), "\n")
    print("Allocation request denial percentage:", bf_mem.get_percentage_denied(), "\n")
    print("Total allocation requests:", bf_mem.get_allocations(), "\n")
    print("Total allocation request denials", bf_mem.get_denied_allocations(), "\n")
    print("Total deallocations:", bf_mem.get_deallocations(), "\n")

def display_next_fit(nf_mem):

    #nf_mem = nf_memory
    #nf_mem = MemoryManagement_2.Next_Fit()
    print()
    print("Total fragments:", nf_mem.get_fragments(), "\n")
    print("Average fragmentations:", nf_mem.get_average_fragmentation(), "\n")
    print("Average allocation time:", nf_mem.get_average_allocation_time(), "\n")
    print("Allocation request denial percentage:", nf_mem.get_percentage_denied(), "\n")
    print("Total allocation requests:", nf_mem.get_allocations(), "\n")
    print("Total allocation request denials", nf_mem.get_denied_allocations(), "\n")
    print("Total deallocations:", nf_mem.get_deallocations(), "\n")

def display_worst_fit(wf_mem):

    #wf_mem = wf_memory
    #wf_mem = MemoryManagement_2.Worst_Fit()
    print()
    print("Total fragments:", wf_mem.get_fragments(), "\n")
    print("Average fragmentations:", wf_mem.get_average_fragmentation(), "\n")
    print("Average allocation time:", wf_mem.get_average_allocation_time(), "\n")
    print("Allocation request denial percentage:", wf_mem.get_percentage_denied(), "\n")
    print("Total allocation requests:", wf_mem.get_allocations(), "\n")
    print("Total allocation request denials", wf_mem.get_denied_allocations(), "\n")
    print("Total deallocations:", wf_mem.get_deallocations(), "\n")