from collections import Counter
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        d= Counter(s)
        arr=[]
        
        maxCtr=0
        for i in range(len(dictionary)):
            j=dictionary[i]
            
            # cheking that s have all letters in j in order
            l1=l2=0
            while l2< len(j) and l1<len(s):
                if j[l2] ==s[l1]:
                    l2+=1
                    l1+=1
                else:
                    l1+=1
            if l2!=len(j):
                continue
            else:
                if len(j)>maxCtr:
                    maxCtr=len(j)
                    arr=[j]
                elif len(j)==maxCtr:
                    arr.append(j)
            # counting the length of j 
#             temp = Counter(list(j))
#             ctr=0
#             brk=True
#             for k,v in temp.items():
                
#                 if k in d and v<= d[k]:
#                     ctr+=v
#                 else:
#                     brk=False
#                     break
#             if brk:
#                 if ctr>maxCtr:
#                     maxCtr=ctr
#                     arr=[j]
#                 elif ctr==maxCtr:
#                     arr.append(j)
        
        if arr:
            arr.sort()
            # print(maxCtr)
            return arr[0]
        else:
            return ""
            
                
                    

        
        