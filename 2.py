'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1,2,3,5,8,13,21,34,55,89,...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''
def fibgen(upr):
    n = 0
    n2 = 1
    list1 = []
    for x in range(1,upr):
        n = n + n2
        n2 = n2 + n
        print "n =", n
        if n > 4000000:
            return list1
        if n % 2 == 0:
            list1.append(n)
            print list1
            #print n2
        if n2 % 2 == 0:
            list1.append(n2)
            print list1
            #print n
        print "n2 =", n2
total = 0
for x in fibgen(4000000):
    total += x
    print "total is", total

print "final total is", total