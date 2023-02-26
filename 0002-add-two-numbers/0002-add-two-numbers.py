# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur=None        
        head=None

        carry=0
        while l1 and l2:
            sums=l1.val + l2.val + carry
            val=0
            s=str(sums)
            if len(s)>1:
                val=int(s[-1])
                carry=int(s[:-1])
                # print(s, carry)
            else:
                val=sums
                carry=0
                
            if cur:    
                cur.next=ListNode(val)
                cur=cur.next
            else:
                cur=ListNode(val)
                head=cur
            
            l1=l1.next
            l2=l2.next
        
        ptr=None
        if l1:
            ptr=l1            
        elif l2:
            ptr=l2
            
        while ptr:
            #calculating the carry value
            sums=ptr.val+carry
            print(ptr.val, sums, carry)
            val=0
            s=str(sums)
            if len(s)>1:
                val=int(s[-1])
                carry=int(s[:-1])                
            else:
                val=sums 
                carry=0
                
            
            cur.next=ListNode(val)
            cur=cur.next
            ptr=ptr.next
        if carry>0:
            cur.next=ListNode(carry)
        return head