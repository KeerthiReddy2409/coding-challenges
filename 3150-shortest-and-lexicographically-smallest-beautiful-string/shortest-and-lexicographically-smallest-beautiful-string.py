class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        c = 0
        ans = float('inf')
        z = ""

        for h in range(len(s)):
            if s[h] == "1":
                c += 1

            while c == k:
                if h - l + 1 < ans:
                    ans = h - l + 1
                    z = s[l:h+1]
                elif h - l + 1 == ans:
                    z = min(z, s[l:h+1])

                if s[l] == "1":
                    c -= 1
                l += 1

        return z