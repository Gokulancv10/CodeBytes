
def Solution(s:str):

	return s[::-1]

print(Solution('Hello'))
print(Solution('World'))
print(Solution('How Are You'))

print('-----------------------')

def Solution(s:str):

	res = ''
	for i in range(len(s)-1, -1, -1):
		res+=s[i]
	return res

print(Solution('Hello'))
print(Solution('World'))
print(Solution('How Are You'))