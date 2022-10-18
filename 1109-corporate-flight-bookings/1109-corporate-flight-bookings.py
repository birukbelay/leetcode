class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        arr=[0]*n
        
        # creating summation 
        for i in range(len(bookings)):
            b=bookings[i]
            st, en, val=b[0], b[1],b[2]
            arr[st-1]+=val
            if en<= len(arr)-1:            
                arr[en]-=val
            # print(i, arr)
        # print(arr)
        temp=0
        for i in range(len(arr)):
            arr[i]+=temp
            temp=arr[i]
            
        return arr
        