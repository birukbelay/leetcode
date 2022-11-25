class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d={} ## stores characters as keys & their index as value
        tot=0 ##current running alue of arr
        L=0 ## index of the first val in the valid arr 
        long=0
        for i in range(len(s)):
            tot+=1
            
            c=s[i]
            ##/ if the value exixts in the dictionary
            if c in d:      
                
                ##/  (to find the length b/n the left pointer and the current invalid point)
                ##/ sub is the index of current repeated value minus index of the last 
                sub=d[c]-L+1
                ## 
                tot-=sub
                ## update the left pointer to the current valid point(start of non repeated array)
                L=d[c]+1
                ## find the smallest index form the dictionary
                m=min(d, key=d.get)
                ## pop it until the minimum is the repeated value
                while m!=c:
                    d.pop(m,None)
                    m=min(d, key=d.get)
                ##/ set the last index of the char to the current value
                d[c]=i
            else:
                ## put the char as key & its index as a value
                d[c]=i
            
            long=max(long, tot)
        return long