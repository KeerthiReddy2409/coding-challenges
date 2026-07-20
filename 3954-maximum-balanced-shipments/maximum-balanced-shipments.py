class Solution:
    def maxBalancedShipments(self, w: List[int]) -> int:
        stack=[]
        ans=0
        for i in range(len(w)):
            if not stack:
                stack.append(w[i])
            else:
                if w[i]>=stack[-1]:
                    stack.append(w[i])
                else:
                    ans+=1
                    while stack:
                        stack.pop()
        return ans
                    
                