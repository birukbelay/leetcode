class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allComb=[]
    
        def backtrack(start, comb):
            if len(comb)==k:
                allComb.append(comb[:])
                return
            for i in range(start, n+1):
                # decision to add a number into the combination
                comb.append(i)
                # decide to remove a num from the combination                
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        return allComb
            