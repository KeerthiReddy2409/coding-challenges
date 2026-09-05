class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=set(nums)
        ans=0
        for i in x:
            if i-1 not in x:
                l=1
                while i+1 in x:
                    i+=1
                    l+=1

                ans=max(ans,l)
        return ans