'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
test1 = 13195
answ = 600851475143

def stolen(n):
    d = 3
    while d*d<n:
        if n%d == 0:
            n/=d
        else:
            d+=2
#        print n
#        print d
    print n

def get_factors(n):
    flist = [n]
    x = 3
    while x*x < n:
        #     print x
        if x % 2 != 0:
            if n % x == 0:
                flist.append(x)
                print flist
        x+=2
    print "flist is ", flist
    print "Ran get_factors()"
    return flist
def checkp(f):
    fl = get_factors(f)
    plist = [0]
    print "defined plist"
    ite = 0
    for x in fl:
        print "loop iteration", ite
        if len(get_factors(x)) == 2:
            plist.append(x)
        ite = ite+1
    print plist
    print "ran checkp()"
stolen(answ)
#checkp(test1)
#get_factors(test1)
