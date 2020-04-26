
# -0.5 because homework is done not in time 

# Task1 ( -0.1 )
l = [ str(x) + str(x+1) for x in range(1,101)]
print(l)


# Task2 ( -0.1 )
l = [ str(x) + str(x*7) for x in range(1, 21) ]
print(l)

# Task3 ( -0.5 )
import random
import time

# I had to use a function
def convert(num):
	return num * 0.621

# name your variables correctly
kilometers = []
miles      = [] 

while(1):
	kilometers.append(random.randint(0, 1000))
	miles.append(convert(kilometers[-1]))
	print('\r', miles, flush=True, end='')
	
	time.sleep(1)


# Task4 ( Nice )
file = open('numbers.txt', 'w')

while True:
	a = int(input())
	if a != 0:
		file.write(str(a) + ' ') # Add space
		print(a*2)
	if a == 0:
		break

file.close()
