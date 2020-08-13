# ECS122A (2019 Winter) Review
# Dynamic Programming

# ---------------------------------------------------------------
# Rod Cutting Problem
 For length  k >= 1,  r_k = max(1<=i<=k) (p_i+ r_(k-i))


def memoization(price, n):
    r =  [-1 for i in n] # float(-"inf")
	return top_down(price, n, r)


def top_down(price, n, r):
	if r[n] >= 0:
		return r[n]
	
	if n == 0:
		max_value = 0
	else
		max_value = -1 # float(-"inf")
		for i in range(0, n):
			max_value = max(max_value, p[i] + top_down(p, n-i, r))
		r[n] = max_value

	return max_value

k = 3
price = [2, 5, 6]
x = memoization(price, k)

print ("Maximum value is "+ str(x))


# ---------------------------------------------------------------
# Subset Sum Problem
"""
def bottom_up(n, bound, weights):
	M = []
	for i in range(n):
		for j in range(bound):
			M[i][j] = 0

	for i in range(n):
		for j in range(bound):
			if j < weights[i]:
				M[i, j] = M[i-1, j]
			else:
				M[i, j] = max(M[i-1, j], weights[i] + M[i-1,j-1])

	return M[n][bound] 


k = 5
W = 8
weights = [5, 9, 1, 3, 6]
x = bottom_up(k, W,weights)

print ("Maximum value is with the bound of " + str(W) + str(x))
"""

# ---------------------------------------------------------------
# Hardcore Park
def memoization(ps):
	M = [float("inf") for i in range(len(ps))]
    M[0] = 5
    return Parkour(ps, M)

def Parkour(ps, memo): # ps list of inputs in tuples
	n = len(ps) - 1
	if memo[n] != float("inf")
		return memo[n]

	else:
		for i in range(1, len(ps)):
			for j in  range(0, len(ps[i])):

				if ps[n][j] < ps[n-1][] and ps[n][j] - ps[n-1][] <  5:
					M[i] = M[i-1] + 1

				elif ps[n][j] == ps[n-1][j]:
					M[i] = M[i-1]						

				elif ps[n][j] > ps[n-1][] and ps[n][j] - ps[n-1][] >  5:
					M[i] = M[i-1] - 1

	memo[n] = min_value
    return min_value


input = [(16, 18, 14), (19, 18, 17), (20, 17, 21), (20, 10, 19), (7, 4, 14), (11, 3, 4), (8, 5, 15, 4), (3, 4, 2, 6), (10, 8, 12), (10, 17, 2, 0, 11, 16)]
a = memoization(input)

print("Total time on the best path: " + str(a))


























