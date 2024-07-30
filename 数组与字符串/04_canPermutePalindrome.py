class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        has_odd = 0
        cnt = Counter(s)
        for v in cnt.values():
            has_odd += (v & 1)
        return has_odd <= 1
