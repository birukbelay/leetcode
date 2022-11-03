class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1=version1.split(".")
        a2=version2.split(".")
        N1=len(a1)
        N2=len(a2)
        maxArr= a1 if N1>N2 else a2
        long, short= max(N1,N2), min(N1, N2)
        for i in range(min(N1, N2)):
            n1, n2 = int(a1[i]), int(a2[i])
            if n1>n2: return 1
            elif n2>n1: return -1
        # print("1fin")
        for i in range(short, long):
            if int(maxArr[i]) >0:
                print("i-",i)
                return 1 if N1>N2 else -1
        return 0

