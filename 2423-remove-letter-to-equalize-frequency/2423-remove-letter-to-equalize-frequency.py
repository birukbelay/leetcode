class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        d={}
        for i in word:
            d[i]= d.get(i, 0) + 1

        for k,v in d.items():
            d[k]-=1
            mp =set(d.values())
            mp.discard(0)         
                

            # mp =set(d.values())
            if len(mp)==1:
                return True
            d[k]= d.get(k, 0)+1
        return False



        
        if len(d)==len(word) or len(d)==1: return True
        # d= dict(sorted(d.items(), key=lambda x:x[1]))
        # lst = list(d.items())
        mp =set(d.values())
        l=len(mp)
        if l>2 : return False
        print(mp)
        if l==1:
            a=word[0]
            if d[a]==1:
                return True
            return False
        lst= list(mp)
        a,b = lst[0], lst[1]
        return True if min(a, b)+1 ==  max(a,b) else False
        

        
        

        
#         a= sorted(d.items(), key=lambda item: item[1])
        
#         s = set(word)
        
#         for i in range(1, len(s)):
#             if 
        # tol=1
        # cur=lst[0][0]
        # # print(d)
        # print(lst)
        # print(mp)
        # for k, v in lst:
        #     # if the keys are the same or value of both indecies are equal pass
        #     if k==cur or d[cur]==v:
        #         continue
        #     if d[cur] == v+1 or d[cur]==v-1:
        #         if tol<1: return False
        #         tol-=1
        #     if d[cur] >v+1 or d[cur]< v-1:
        #         return False
        
        # if tol==1: return False
        # return True
                
                
                
        