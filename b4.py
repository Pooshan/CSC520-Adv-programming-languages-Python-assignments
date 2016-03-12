

import itertools
from itertools import permutations

"""
n = input("Enter value of n: ")
#k = input("Enter value of k: ")
k = 2

def kbits(n, k):
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return result

print(kbits(int(n),int(k)))

#Output: ['1110', '1101', '1011', '0111']



def combinations(iterable, r):
    #def __str__(self):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

print(combinations(iterable, r))

"""

n = input("Enter the value of n: ")
"""
# your code goes here
def permutation(n):
	for i in range(1 << n):
		s = bin(i)[2:]
		s = '0'*(n-len(s))+s
		print (map(int,list(s)))
	#print permutation(int(n))

#permutation(2)

print('0'*1+bin(1)[2:])
"""


def binPermute(n):
	if n==0:
		return []
	elif n==1:
		return ['0','1']
	else:
	  # -- append o and 1 and recuse call binPermute(n-1)
	  return ['0'+x for x in binPermute(n-1)]+['1'+x for x in binPermute(n-1)]


print(binPermute(int(n)))
