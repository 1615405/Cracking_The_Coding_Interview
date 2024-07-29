class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        cnt = defaultdict(int)
        for char_1 in s1:
            cnt[char_1] += 1
        for char_2 in s2:
            cnt[char_2] -= 1
        return all(cnt[c] == 0 for c in cnt.keys())
