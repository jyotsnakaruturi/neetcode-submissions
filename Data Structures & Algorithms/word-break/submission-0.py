class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordDict=set(wordDict)
        dp=[False]*(n+1)
        maxlen=0
        for i in wordDict:
            maxlen=max(maxlen,len(i))
        dp[0]=True
        for i in range (1,n+1):
            for j in range (max(0,i-maxlen),i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[n]

        