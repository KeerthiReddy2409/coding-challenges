class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # if sum(nums1)!=sum(nums2):
        #     return -1
        # if nums1==nums2:
        #     return 0
        # if k==0:
        #     return -1
        # ans=0
        # for i in range(len(nums1)):
        #     if abs(nums1[i]-nums2[i])%k==0:
        #         ans+=abs(nums1[i]-nums2[i])//k
        #     else:
        #         return -1
        # if ans==0:
        #     return -1
        # return ans//2


        if k == 0:
            return 0 if nums1 == nums2 else -1

        pos = 0
        neg = 0

        for a, b in zip(nums1, nums2):
            diff = a - b

            if diff % k != 0:
                return -1

            if diff > 0:
                pos += diff // k
            else:
                neg += (-diff) // k

        return pos if pos == neg else -1