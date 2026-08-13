class Solution:
    def numberOfUniqueGoodSubsequences(self, s: str) -> int:
        dp0 = dp1 = 0
        zero = False

        for c in s:
            if c == '1':
                dp1 = dp0 + dp1 + 1
            else:
                dp0 = dp0 + dp1
                zero = True

        return (dp0 + dp1 + zero) % (10**9 + 7)