'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

list1 = []
high = 0
for x in range(100,1000):
    for x2 in range (100,1000):
        y = x*x2
#        print y, x, x2
        if str(y) == str(y)[::-1]:
            if y > high:
                list1.append(y)
                high = y
print list1
