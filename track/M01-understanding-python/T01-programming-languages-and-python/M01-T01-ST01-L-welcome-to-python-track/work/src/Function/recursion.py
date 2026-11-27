def display_s_n_times(s,n):
    if n<1:
        return 
    print(s)
    display_s_n_times(s-1,n-1)

display_s_n_times(21,7)