class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l=1
        h=max(price)
        def f(x,k):
            a=0
            for i in range(1,len(price)):
                if price[i]-price[a]>=x:
                    k-=1
                    a=i
                if k==1:
                    return True
            return False
                    
        while l<=h:
            mid=(l+h)//2
            if f(mid,k):
                l=mid+1
            else:
                h=mid-1
        return h
            