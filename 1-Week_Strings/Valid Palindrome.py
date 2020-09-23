def valid_palindrome(s):
	
	s1 = ''.join(filter(str.isalpha,s)).lower()
	return s1 == s1[::-1]

print(valid_palindrome("A Man, a Plan, a Canal: Panama"))
print('-----------------------')
def is_valid_palindrome(s):

	s1 = [i for i in s if i.isalpha()]
	s2 = s1[:len(s1)//2]
	s3 = s1[len(s1)//2:]
	d = {}
	for i in range(len(s2)):
		if s1[i] in d:
			d[s1[i].lower()] +=1
		else:
			d[s1[i].lower()] = 1

	for i in s3:
		if i.lower() in d:
			d[i.lower()]-=1

	flag = 0
	for i in d:
		if d[i]>0:
			flag = 1
			print('Not A Palindrome')
			break;
		else:
			flag = 0
	if flag==0:
		print('It\'s a Palindrome')
	# print(d)
	# print(s2)
	# print(s3)
is_valid_palindrome("A Man, a Plan, a Canal: Panama")
is_valid_palindrome("animal")