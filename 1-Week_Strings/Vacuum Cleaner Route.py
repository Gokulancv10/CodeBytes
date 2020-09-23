"""
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes,
return whether or not it will return to its original position. The string will only contain L, R, U, and D characters,
representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

def solution(s:str):

	res = 0
	for i in s:
		if i=='L' or i =='U':
			res+=1
		else:
			res-=1

	if res!=0:
		return False
	else:
		return True

print(solution('LR'))
print(solution('URURD'))
print(solution('RUULLDRD'))

print('-------------------')

def solution(s:str):

	return s.count('L')+s.count('U') == s.count('D')+s.count('R')

print(solution('LR'))
print(solution('URURD'))
print(solution('RUULLDRD'))

