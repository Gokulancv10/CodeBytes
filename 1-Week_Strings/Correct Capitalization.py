"""
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

def solution(s):

    return True if s==s.capitalize() or s==s.upper() or s==s.lower() else False

print(solution('USA'))
print(solution('Calvin'))
print(solution('compUter'))
print(solution('coding'))