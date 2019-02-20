import MemoryManagement_2, Request_Generator, Stats_Report

def main():

    print("TEST")
    ff_memory = MemoryManagement_2.First_Fit()
    bf_memory = MemoryManagement_2.Best_Fit()


    num_requests = 10000
    
    Request_Generator.generator(ff_memory, bf_memory, nf_memory, wf_memory, num_requests)
    print("Statistics for", num_requests, "allocation requests:\n")
    
    # Display first fit.
    print("First fit:\n")
    ff_memory.print()
    print()
    Stats_Report.display_first_fit(ff_memory)
    print()
    print()

    # Display best fit.
    print("Best fit:\n")
    bf_memory.print()
    print()
    Stats_Report.display_best_fit(bf_memory)
    print()
    print()

    # Display next fit.
    print("Next fit:\n")
    nf_memory.print()
    print()
    Stats_Report.display_next_fit(nf_memory)
    print()
    print()

    # Display worst fit.
    print("Worst fit:\n")
    wf_memory.print()
    print()
    Stats_Report.display_worst_fit(wf_memory)
    print()
    print()


main()
