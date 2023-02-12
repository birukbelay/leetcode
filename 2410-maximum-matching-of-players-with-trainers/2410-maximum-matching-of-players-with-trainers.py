class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ctr=0
        P=len(players)-1
        T=len(trainers)-1
        
        while P>=0 and T>=0:
            
            while  P>=0 and T>=0 and trainers[T]>= players[P]:
                ctr+=1
                P-=1
                T-=1
            while  P>=0 and trainers[T]< players[P]:
                P-=1
        return ctr

        