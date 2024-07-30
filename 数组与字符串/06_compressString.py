class Solution:
    def compressString(self, s: str) -> str:
        ans = ""
        i = 0

        while i < len(s):
            cnt = 1
            c = s[i]
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                cnt += 1
            ans += c + str(cnt)
            i += 1
        
        return ans if len(ans) < len(s) else s
