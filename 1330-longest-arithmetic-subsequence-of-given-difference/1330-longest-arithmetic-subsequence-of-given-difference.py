class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp = {}
        # answer = 1
        # for a in arr:
        #     before_a = dp.get(a - difference, 0)
        #     dp[a] = before_a + 1
        #     answer = max(answer, dp[a])
            
        # return answer
        memo= {}
        def solve(i):
            # if i>=len(arr)-1:
            #     # memo[i]=cnt
            #     return cnt
            nxt= arr[i]+difference
            if nxt in memo:
                memo[arr[i]]= memo[nxt] +1
            else:
                memo[arr[i]]=1
            
            # if (arr[i]-num)==difference:
                
            #     num=arr[i]
            #     cnt+=1
            # memo[i]= solve(i+1, num, cnt)
            return memo[arr[i]]
        res =0
        for i in range(len(arr)-1, -1, -1):
            res = max(res, solve(i))
        return res
            