from collections import Counter

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)

        g = 0
        for count in freq.values():
            g = self.gcd(g, count)

        return g > 1