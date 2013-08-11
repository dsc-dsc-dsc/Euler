'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
x = 1
y = 512
list1 =[]
z = True
while 7:
    if z == True:
        y+=y/16
    if y > 8217728:
        z = False
    if z == False:
        y-=y/2
    if y < 1000000:
        z = True
    p = True
    print y/512
    for div in range (2, y):
        if y/div == int(y/div):
            p = True
    x+=1
print list1
