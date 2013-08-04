'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
test1 = 13195
answ = 600851475143

def get_factors(n):
    flist = [n]
    for x in range(1,n):
        #     print x
        if n % x == 0:
            flist.append(x)
            print flist
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
checkp(answ)
#get_factors(test1)
