class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dp[i] = true if we can reach s[i]
        dp = [v == '0' for v in s]
        
        # pre means the number of previous position that we can jump from.
        pre = 0
        
        for i in range(1, len(s)):
            if i >= minJump:
                pre+= dp[i - minJump]
            if i > maxJump:
                pre -= dp[i- maxJump -1]
            dp[i] = pre > 0 and s[i] == '0'
        return dp[-1]