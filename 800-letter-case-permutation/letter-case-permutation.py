class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(i, curr):
            if i == len(s):
                ans.append("".join(curr))
                return

            if s[i].isdigit():
                curr.append(s[i])
                backtrack(i + 1, curr)
                curr.pop()
            else:
                curr.append(s[i].lower())
                backtrack(i + 1, curr)
                curr.pop()

                curr.append(s[i].upper())
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return ans