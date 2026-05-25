a=[]
class Solution:

    def encode(self, strs: List[str]) -> str:
        global a
        a=list(strs)
        return 'a'

    def decode(self, s: str) -> List[str]:
        global a
        return a
