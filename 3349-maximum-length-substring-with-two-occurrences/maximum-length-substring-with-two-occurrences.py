class Solution:
    def maximumLengthSubstring(self,s:str)->int:
        x={}
        l=ans=0
        for i in range(len(s)):
            x[s[i]]=x.get(s[i],0)+1
            while x[s[i]]>2:
                x[s[l]]-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans