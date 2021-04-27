a = []
m = int(input("los multiplos de = "))
for num in range(int(input("cantidad de multiplos de {} = ".format(m)))):
    a.append(num*m)
for x in range(len(a)):
    print("{} * {} = {}".format(m,x,a[x]))