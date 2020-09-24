"""
This question is asked by Google. Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

def solution(nums1, nums2):

    res = [i for i in nums2 if i in nums1]
    return res

print(solution(nums1 = [2, 4, 4, 2], nums2 = [2, 4]))
print(solution(nums1 = [1, 2, 3, 3], nums2 = [3, 3]))
print(solution(nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7]))

print('-------------------------------')

from collections import Counter
def solution(nums1, nums2):

    a,b = map(Counter, (nums1, nums2))

    return list((a & b).elements())
    

print(solution(nums1 = [2, 4, 4, 2], nums2 = [2, 4]))
print(solution(nums1 = [1, 2, 3, 3], nums2 = [3, 3]))
print(solution(nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7]))

print('-------------------------------')

from collections import Counter
def solution(nums1, nums2):

    counts = Counter(nums1)
    res = []
    for i in nums2:
        if counts[i]>0:
            res.append(i)
            counts[i]-=1
    return res

print(solution(nums1 = [2, 4, 4, 2], nums2 = [2, 4]))
print(solution(nums1 = [1, 2, 3, 3], nums2 = [3, 3]))
print(solution(nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7]))