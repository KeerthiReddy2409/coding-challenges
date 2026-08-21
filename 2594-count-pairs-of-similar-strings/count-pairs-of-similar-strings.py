from collections import Counter

class Solution:
    def similarPairs(self, words):
        c = Counter(tuple(sorted(set(w))) for w in words)

        ans = 0
        for k in c.values():
            ans += k * (k - 1) // 2

        return ans