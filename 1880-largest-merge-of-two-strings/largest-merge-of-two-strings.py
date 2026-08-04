class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        ans = ""
        i = j = 0
        n, m = len(w1), len(w2)

        while i < n and j < m:
            if w1[i:] > w2[j:]:
                ans += w1[i]
                i += 1
            else:
                ans += w2[j]
                j += 1

        ans += w1[i:]
        ans += w2[j:]

        return ans