import random
from Crypto.Util import number
import gensafeprime
import numpy as np

rand = random.SystemRandom()

def generate_prime(n):
	if (n==2):
		p = 2
		g = 1
	elif (n==3):
	    p = 5
	    g = 2
	elif (n==4):
	    p = 11
	    g = 2
	elif (n==5):
	    p = 23
	    g = 11
	else:
		p = gensafeprime.generate(n)
		q = (p-1)//2

		t = 1
		while t == 1:
			h = number.getRandomRange(2,p-2)
			t = pow(h,2,p)

		g = h

	return (p,g)

def create_data(k,b,p):
	data = []
	for i in range(k):
		data.append(rand.getrandbits(b)%p)

	return data


def create_blocks(n,data,p):

	blocks = []
	ids = []
	poly_value = 0
	for i in range(1,n+1,1):
		poly_value = 0
		for j in range(k):
			poly_value += ((data[j]%p)*(pow(i,j,p)%p))%p
		blocks.append(poly_value%p)
		ids.append(i)

	return (ids,blocks)

def reconstruct_coefficients(x,y,p):
	M=np.ones(k*k).reshape((k,k))
	for i in range(k):
	    a=x[i]
	    for j in range(1,k,1):
	        M[i][j]=pow(a,j,p)

	y=np.array(y)
	# y=y[0:k]
	M=np.linalg.inv(M)
	M=np.dot(M,y)

	coef=[]
	for i in M:
	    coef.append(int(round(i)))

	# print(coef)

	return coef


b = 10
k = 5

# p = gensafeprime.generate(256)
p,g = generate_prime(100)

data = create_data(k,b,p)


n = 8

ids,blocks = create_blocks(n,data,p)
coef = reconstruct_coefficients(ids[3:],blocks[3:],p)


print(data)
print(coef)


