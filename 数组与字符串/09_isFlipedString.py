class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return s1 in (s2 + s2) if len(s1) == len(s2) else False
