"""
jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""

def solution(jewels, stones):
	res = 0
	for i in jewels:
		res += stones.count(i)
	return res

print(solution("abc", "ac"))
print(solution("Af", "AaaddfFf"))
print(solution("AYOPD", "ayopd"))

print('--------------------------')

def solution(jewels, stones):
	d = {}

	for i in stones:
		if i in d:
			d[i]+=1
		else:
			d[i] = 1

	res = 0
	for i in jewels:
		if i in d:
			res+=d[i]
	return res

print(solution("abc", "ac"))
print(solution("Af", "AaaddfFf"))
print(solution("AYOPD", "ayopd"))