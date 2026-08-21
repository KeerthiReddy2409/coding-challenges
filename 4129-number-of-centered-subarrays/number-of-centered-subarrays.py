class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            s=set()
            a=0
            for j in range(i,len(nums)):
                a+=nums[j]
                s.add(nums[j])
                if a in s:
                    ans+=1
        return ans
