class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store=[0] * 26
        for i in s:
            c= ord(i) - ord('a')
            store[c]=store[c]+1
        for i in t:
            c = ord(i) - ord('a')
            store[c]=store[c]-1
        for i in store:
            if not i==0:
                return False
        return True
        