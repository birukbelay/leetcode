class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        l,r=0,len(skill)-1
        tot=0
        pt=skill[0] + skill[-1]
        while l<=r:
            # print(l, skill[l], skill[r] )
            if skill[l] + skill[r] == pt:
                tot+= (skill[l] * skill[r])
            else:
                return -1
            l+=1
            r-=1
        return tot
            
        
        