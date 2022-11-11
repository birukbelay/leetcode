class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')':
                val = stack[-1]
                
                if val=='(':
                    stack.pop()
                    stack.append(1)
                elif type(val) == (int or float):
                    score=0
                    while stack and type(stack[-1]) == (int or float):
                        score += stack.pop()
                    if stack and stack[-1] =='(':
                        stack.pop()
                        score*=2
                        stack.append(score)
        # print('st-',stack)
        return sum(stack)
                
                
                
                
            
        