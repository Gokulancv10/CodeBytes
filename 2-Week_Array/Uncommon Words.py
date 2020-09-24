"""
This question is asked by Amazon. Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""

from collections import Counter
from itertools import chain
def solution(s1:str, s2:str):

	res = [word for word, cnt in Counter(chain(s1.split(), s2.split())).items() if cnt==1]
	return res

print(solution("the quick", "brown fox"))
print(solution("the tortoise beat the haire", "the tortoise lost to the haire"))
print(solution("copper coffee pot", "hot coffee pot"))

print('-------------------------------------')

def solution(s1:str, s2:str):

	c = Counter((s1 + ' '+ s2).split())
	return [w for w in c if c[w]==1]

print(solution("the quick", "brown fox"))
print(solution("the tortoise beat the haire", "the tortoise lost to the haire"))
print(solution("copper coffee pot", "hot coffee pot"))

print('--------------------------------')

def solution(A:str, B:str):
	return [s for s, v in Counter(A.split() + B.split()).items() if v == 1]

print(solution("the quick", "brown fox"))
print(solution("the tortoise beat the haire", "the tortoise lost to the haire"))
print(solution("copper coffee pot", "hot coffee pot"))