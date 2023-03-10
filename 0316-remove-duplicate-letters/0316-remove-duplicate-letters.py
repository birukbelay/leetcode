class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        d= collections.Counter(list(s))

        stack=[]
        st=set()
        for i in range(len(s)):
            
            val=s[i]
            # print(stack, val,d)
            if val in st: 
                d[val] -= 1
                continue
                
            while stack and stack[-1] >= val and d[stack[-1]]>1 :
                d[stack[-1]]-=1
                
                if stack[-1] in st and val not in st:
                    st.discard(stack.pop())
                
            if val not in st:   
                stack.append(val)
                st.add(val)
        return "".join(stack)
            
            

#         d= collections.Counter(list(s))
#         stack=[]
#         st=set()
#         for i in range(len(s)):
#             val=s[i]
            
#             if val in st: 
#                 d[val] -= 1
#                 continue
#             while stack and stack[-1] >= val and d[stack[-1]]:
#                 st.remove(stack.pop())
#             d[val] -= 1
            
#             if val not in st:
#                 stack.append(val)
#                 st.add(val) 
#         return ''.join(stack)
        
        
        
        
        
#         #creating 
#         small=s[-1]
#         for i in range(len(s)-1, -1, -1):            
            
#             if s[i]> small:
#                 newS= small + newS
#             else:
#                 newS = s[i] + newS
#                 small=s[i]
#             # if s[i] not in d:
#         # print(newS)
#         ans=''
#         for i in range(len(s)):
#             val=s[i]
#             if val> newS[i]:
#                 continue
#             else:
#                 ans+=val
            
                
            
        