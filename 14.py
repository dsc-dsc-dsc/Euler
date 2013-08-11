'''

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    '''
st = 27
en = 1000000
#en = 1000
#en = 27
start = 0

mx = 0


def  collatz(n):
    #print "starting at", n
    i = 1    
    while (n>1):
        if not n%2:
            n = n/2
        else:
            n = 3*n+1
#        print n, "working... (iteration", i, ")"
        i = i+1
    #print "that took", i, "iterations"
    return i
while (st <= en):
    i = collatz(st)
    st = st + 1
    if mx < i:
        mx = i
        start = st - 1
        #print "lel"
 #   print "max is", mx, "from", start
#print itera
print mx, start
