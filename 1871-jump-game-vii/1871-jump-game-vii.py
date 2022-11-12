class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dp[i] = true if we can reach s[i]
#         dp = [v == '0' for v in s]
        
#         # pre means the number of previous position that we can jump from.
#         pre = 0
        
#         for i in range(1, len(s)):
#             if i >= minJump:
#                 pre+= dp[i - minJump]
#             if i > maxJump:
#                 pre -= dp[i- maxJump -1]
#             dp[i] = pre > 0 and s[i] == '0'
#         return dp[-1]
    
        # bfs -------------------------------------------
        q, farthest = deque([0]), 0
        
        while q:
            i=q.popleft()
            start = max(i + minJump, farthest +1)
            end = min(i + maxJump +1, len(s)) # so it is not out fo bound
            for j in range(start, end):
                if s[j]=='0':
                    q.append(j)
                    if j == len(s)-1:
                        return True
            farthest = i+ maxJump
        return False
        