class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mp = {')': '(', '}': '{', ']': '['}

        for c in s :
            if c not in mp:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != mp[c]:
                        return False

        return not stack





        





