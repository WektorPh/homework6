#Task1
l = [x for x in range(0, 101, 2)]
print(l)
 #Task2
a = [x for x in range(57, 139, 2)]
print(a)
#Task3
b = [2 ** x for x in range(30)]
print(b)
#Task4
c =[x for x in range(-100, 99)]
print(c)
#Task5
d = [200 for x in range(87)]
print(d)
#Task6
C = [x for x in range(0, 100)]
F = [x * 1.8 + 32 for x in C]
print(F)
#Task7
import random
k = [(random.randint(1, 200), random.randint(1, 200)) for x in range(100)]
print(k)
def lesser(num):
	return int(num[0]/num[1])

p = list(map(lesser, k))
print(p)




