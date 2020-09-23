"""
"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"""

def solution(s:str):

	if s==s[::-1]:
		return True

	l = list(s)
	print('list: ',l)

	flag = 0
	for i in range(len(l)):
		res = l.pop(i)
		print('Removed Element: ',res)
		print(l)
		print()
		if l == l[::-1]:
			flag = 1
			return True, ''.join(l)
			break;
		else:
			l.insert(i, res)

	return False

# print(solution('abcba'))
# print(solution('foobof'))
# print(solution('abccab'))
print(solution('abcicb'))