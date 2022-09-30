class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
        
#         d = {}
#         cnt = 0
#         l= 0
#         maxf = 0 
#         for r in range(len(s)):
#             i=s[r]
#             d[s[r]]= 1 + d.get(s[r],0)
            
#             maxf=max(maxf, d[s[r]])
#             if (r - l + 1) - maxf >k:
#                 d[s[r]] -=1
#                 l+=1
#             cnt = max(cnt, r - l + 1)
#         return cnt
        
        
        
        
#         ok=k
#         l=0
#         tot=0
#         ctr=0
#         c=s[0]
#         for i in range(len(s)):            
#             if s[i]==s[l]:
#                 ctr+=1                
#             else:                
#                 if k>0:
#                     k-=1
#                     ctr+=1
#                 else:
#                     print("i",i, s[i])                    
#                     while  s[l]==c:
#                         print("l,s[l]=",l,s[l])
#                         if ok!=0:k+=1
#                         l+=1
#                         # ctr-=1
#                     c=s[l]
#                     ctr=1
#                     print("c-",c)
                    
#             tot=max(ctr, tot)
#         return tot
                    
                        