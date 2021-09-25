# SortingArray
#This is a python code for sorting n numbers of a sequence in increasing order.
def Sort(seq): #sorts an array of n elements
    n=len(seq)
    stop=1
    while stop==1:
        stop=0
        for j in range(2):
            for i in range(0,n-1-j,2):
                    if seq[i+j]>seq[i+j+1]:
                        seq[i+j], seq[i+j+1] = seq[i+j+1], seq[i+j]
                        stop=1
    return seq
