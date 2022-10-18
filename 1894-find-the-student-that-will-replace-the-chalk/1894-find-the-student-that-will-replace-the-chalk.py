class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s,i=0,0
        ckS=sum(chalk)
        reminder= k %ckS
        # print(reminder)
        while reminder>0:
            reminder-=chalk[i]
            if reminder<0:
                return i
            # print(i,reminder)
            i+=1
            # if i>=len(chalk):
            #     i=0
        return i
            