# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0,head)
        
        l,r = head,head.next
        while r:
            if r.val>= l.val:
                l,r = r,r.next 
                continue
                
            ptr=dum
            while r.val > ptr.next.val:
                ptr=ptr.next
            
            l.next=r.next          
           
            r.next=ptr.next
            ptr.next=r
            r=l.next
        return dum.next