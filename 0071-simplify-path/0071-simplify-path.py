class Solution:
    def simplifyPath(self, path: str) -> str:
        # to remove multiple /
        while '/./' in path:
            path=path.replace('/./','/')
        # print(path)
        newS=''
        sFound=False
        for i in range(len(path)):            
            if path[i]=='/':
                if sFound:
                    continue
                else:
                    newS+=path[i]
                sFound=True
                
            else:
                sFound=False
                newS+=path[i]
        # print(newS)
        s=newS.split('/')
        print(s)
        stack=[]
        for i in s:            
            if i=='..':
                if stack: stack.pop()
            elif i !="" and i!='.':
                stack.append(i)
        return '/' +'/'.join(stack)
            
                

        
        
                
        
        