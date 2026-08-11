class Solution:
    def interpret(self, command: str) -> str:
        i=0
        ans=""
        n=len(command)
        while i<n:
            if command[i]=="G":
                ans+="G"
                i+=1
            else:
                if i+1<n and command[i+1]==")":
                    ans+="o"
                    i+=2
                else:
                    ans+="al"
                    i+=4
        return ans
