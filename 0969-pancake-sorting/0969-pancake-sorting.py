def checkArrEqual(arr1, arr2):
    
    for i  in range(len(arr1)):
        if (arr1[i] != arr2[i]):
            return False
    return True
def findMaxIndex(arr):
    max=0
    for i in range(len(arr)):
        if arr[i]>arr[max]:
            max=i
    return max

def reverseArr(arr):
    end = len(arr)-1
    for i in range(len(arr)//2):
        arr[i], arr[end]=arr[end], arr[i]
        end-=1
    return arr 

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        pankaceArr=[]
        # the last index
        lastIndex=len(arr)
        # the sorted arr
        orgArr=arr[:]
        sortedArr=arr[:]    
        workingArr=arr[:lastIndex]
        sortedArr.sort()
           
        final=0
        while not checkArrEqual(sortedArr, arr) and final<len(orgArr)*2:
            # print("=========>>>>>>>>>here, ```S==",final)
        #     # find the max value in the arr
            index = findMaxIndex(workingArr) 
            # the first arr to be reversed 
            arrToBeReversed=workingArr[0:index+1]           
            reverseArr(arrToBeReversed)           
            # concconcatinating the reversed part and the whole part
            # concatArr=arrToBeReversed + workingArr[index+1:]
            # newArr == the Big Int reversed to last arr
            newArr=reverseArr(arrToBeReversed + workingArr[index+1:])       

            pankaceArr.append(index+1)
            pankaceArr.append(lastIndex) 

            arr=newArr+arr[lastIndex:]
            lastIndex-=1
            workingArr=arr[:lastIndex]
            
            # print("arr=", arr,"workingArr=",workingArr, "newArr", newArr)
            final+=1

        # print("conditiov====>2", checkArrEqual(sortedArr, arr))
        return pankaceArr