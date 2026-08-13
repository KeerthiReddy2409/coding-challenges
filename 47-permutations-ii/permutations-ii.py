class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(path, used):
            if len(path) == len(nums):
                ans.add(tuple(path[:]))
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack(path, used)

                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return [list(x) for x in ans]