class Solution:
    def maxDepthAfterSplit(self, s: str) -> list[int]:
        depth = 0
        ans = []

        for c in s:
            if c == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1
        return ans