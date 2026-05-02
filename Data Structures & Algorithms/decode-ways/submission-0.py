class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        if s[0] != "0":
            dp[1]=1

        for i in range (2,n+1):
            oned=int(s[i-1:i])
            twod=int(s[i-2:i])
            if oned>0 and oned<=9 :
                dp[i]+=dp[i-1]
            if twod >= 10 and twod<=26:
                dp[i]+=dp[i-2]
        return dp[n]

        