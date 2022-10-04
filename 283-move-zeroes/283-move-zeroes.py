from datetime import datetime


class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        
#         l=len(nums)

#         zeroArr=[]
#         copyArr=[]
        
#         for i in range(l):
#             if nums[i]==0:
#                 zeroArr.append(0)                
#             else:
#                 copyArr.append(nums[i])
#         cp=len(copyArr)
#         for i in range(len(copyArr)):
#             nums[i]=copyArr[i]
#         for i in range(len(zeroArr)):
#             nums[cp+i]=0

# #         -------------------------------
       
        L = 0
        for i  in range(len(nums)):
            if nums[i] != 0:
                if i != L:
                    nums[i], nums[L] = nums[L] , nums[i]
                L +=1 

        # i=0
        # ctr=0
#         d={}
#         for i in range(l):
            
        
#         while i<l:
#             if nums[i] ==0:
#                 j=i
#                 print(j)
#                 while nums[j+1]!=0 and j<l-1:
#                     nums[j], nums[j+1]=nums[j+1], nums[j]
#                     j+=1
#                 # print("i-",i, "nums-", nums)
#             ctr+=1
#             if ctr>l:
#                 return
#             if nums[i]!=0:
#                 # print(i)
#                 i+=1    
            
        
        
            

