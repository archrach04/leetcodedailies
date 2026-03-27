# Last updated: 3/28/2026, 12:55:13 AM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        max_len=max(len(word) for word in wordDict)
        for i in range(1,n+1):
            for l in range(1,max_len+1):
                if i-l>=0 and dp[i-l]==True:
                    if s[i-l:i] in wordSet:
                        dp[i]=True
                        break
        return dp[n]

