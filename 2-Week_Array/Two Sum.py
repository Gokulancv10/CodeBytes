"""
[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""


def two_sum(a, k):

	d = {}
	for i, num in enumerate(a):
		sub = k - num
		if sub in d:
			return True
		d[num] = i
	return False

print(two_sum([1, 3, 8, 2], 10))
print(two_sum([3, 9, 13, 7], 8))
print(two_sum([4, 2, 6, 5, 2], 4))

print('------Using Two Loops-------')

def two_sum(a, k):

	for i in range(len(a)):
		for j in range(i):
			if a[i] + a[j] == k:
				return True
	return False

print(two_sum([1, 3, 7, 2], 10))
print(two_sum([3, 9, 10, 7], 8))
print(two_sum([4, 2, 6, 5, 2], 4))