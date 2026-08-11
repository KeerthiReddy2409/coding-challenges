class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        s = ans = 0

        for x in nums:
            s += x
            if s - target in seen:
                ans += 1
                seen = {s}
            else:
                seen.add(s)

        return ans