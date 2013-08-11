a = 0
b = 0
for x in range(1,101):
    a+=x*x
for x in range(1,101):
    b+=x
b*=b
print b-a
