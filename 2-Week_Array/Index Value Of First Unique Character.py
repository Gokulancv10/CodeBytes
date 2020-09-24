"""
This question is asked by Microsoft. Given a string, return the index of its first unique character.
If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""

def solution(s:str):

    d = {}

    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1

    for i in d:
        if d[i]==1:
            return s.index(i)
    return -1

print(solution("abcabd")) # 2
print(solution("thedailybyte")) # 1
print(solution("developer")) # 0


print('--------Worst Solution TLE-----------')
def solution(s:str):
    
    for i in s:
        if s.count(i)==1:
            return s.index(i)
    return -1

print(solution("abcabd")) # 2
print(solution("thedailybyte")) # 1
print(solution("developer")) # 0


from collections import Counter

print('---------Best Solution O(n) and O(1)---------')
def solution(s:str):
    
    count = Counter(s)
    print(count)
    
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx

    return -1
    

print(solution("abcabd")) # 2
print(solution("thedailybyte")) # 1
print(solution("developer")) # 0

print('---------Using Set Function---------')
def solution(s:str):
    
    visited = set()

    for i in range(len(s)):
        if i not in visited:
            visited.add(s[i])

            if s.count(s[i])==1:
                return i
    return -1


print(solution("abcabd")) # 2
print(solution("thedailybyte")) # 1
print(solution("developer")) # 0