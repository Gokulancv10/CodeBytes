"""
s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""
print('------Method 1: Using iterator IN Function--------')
def solution(s:str, t:str):

    count = 0
    for i in s:
        if i in t:
            count+=1
    
    if count==len(s) and count==len(t):
        return True
    else:
        return False

print(solution("cat", "tac"))
print(solution("listen", "silent"))
print(solution("program", "function"))
print()

print('----Method 2: Using Dictionary/ Hash Map-------------')

def solution(s:str, t:str):

    d = {}

    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1

    for i in t:
        if i in d:
            d[i]-=1
    
    return all(val==0 for val in d.values())

print(solution("cat", "tac"))
print(solution("listen", "silent"))
print(solution("program", "function"))
print()

print('------Method 3: Using Sorted Function---------')

def solution(s:str, t:str):

    return sorted(s) == sorted(t)

print(solution("cat", "tac"))
print(solution("listen", "silent"))
print(solution("program", "function"))
print()

print('-------Method 4: Usingb Collection.counter-------')

from collections import Counter

def solution(s:str, t:str):

    return Counter(s) == Counter(t)

print(solution("cat", "tac"))
print(solution("listen", "silent"))
print(solution("program", "function"))