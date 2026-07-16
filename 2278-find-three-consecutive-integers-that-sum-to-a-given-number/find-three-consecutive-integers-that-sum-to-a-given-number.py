class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # l=0
        # h=num
        # while l<=h:
        #     mid=(l+h)//2
        #     if mid+2<=h:
        #         l1=3*mid+3
        #     else:
        #         l1=0
        #     if mid-2>=l:
        #         l2=3*mid-3
        #     else:
        #         l2=0
        #     if mid+1<=h and mid-1>=l:
        #         l3=3*mid
        #     else:
        #         l3=0
            
        #     if l1!=0 and l1==num:
        #         return [mid,mid+1, mid+2]
        #     elif l2!=0 and l2==num:
        #         return [mid-2,mid-1, mid]
        #     elif l3!=0 and l3==num:
        #         return [mid-1,mid,mid+1]

        #     elif l1>num and l2>num and l3>num:
        #         h=mid-1
        #     elif l1<num and l2<num and l3<num:
        #         l=mid+1
        #     else:
        #         return []
        if num % 3 != 0:
            return []

        mid = num // 3
        return [mid - 1, mid, mid + 1]