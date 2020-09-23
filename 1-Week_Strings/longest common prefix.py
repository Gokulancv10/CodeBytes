""" 
["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""

def longestCommonPrefix(arr):
    
    prefix = []
    n = len(arr)
    for i in zip(*arr):
        if len(set(i))==1:
            prefix.append(i[0])
        else:
            break

    return ''.join(prefix) if prefix else ''

print(longestCommonPrefix(["colorado", "color", "cold"]))
print(longestCommonPrefix(["a", "b", "c"]))
print(longestCommonPrefix(["spot", "spotty", "spotted"]))
print('-----------------------------')

def longestCommonPrefix1(arr):
    
    m = min(arr)
    M = max(arr)
    i = 0
    for i in range(min(len(m), len(M))):
        if m[i]!=M[i]:
            break
        else:
            i+=1
    return m[:i]

print(longestCommonPrefix1(["colorado", "color", "cold"]))
print(longestCommonPrefix1(["a", "b", "c"]))
print(longestCommonPrefix1(["spot", "spotty", "spotted"]))
print('------------------------------')

def longestCommonPrefix(arr):
    short = min(arr, key=len)

    for i, ch in range(short):
        for j in arr:
            if j[i]!=ch:
                return short[:i]
    return short

print(longestCommonPrefix1(["colorado", "color", "cold"]))
print(longestCommonPrefix1(["a", "b", "c"]))
print(longestCommonPrefix1(["spot", "spotty", "spotted"]))