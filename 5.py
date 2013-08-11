'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
num = 1000000000
list1 = []
for x in range(1,num):
    c = 0
    for i in range(1,21):
        if x % i == 0:
            c+=1
    if c == 20:
        list1.append(x)
        print x
        exit()
print list1
