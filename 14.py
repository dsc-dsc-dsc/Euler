mx = 0
def  collatz(n):
    #print "starting at", n
    i = 1    
    while (n>1):
        if not n%2:
            n = n/2
        else:
            n = 3*n+1
        #print n, "working... (iteration", i, ")"
        i = i+1
    #print "that took", i, "iterations"
    return i
st = 27
en = 1000000
#en = 1000
#en = 27
start = 0
while (st <= en):
    i = collatz(st)
    st = st + 1
    if mx < i:
        mx = i
        start = st - 1
    print "max is", mx, "from", start
#print itera

