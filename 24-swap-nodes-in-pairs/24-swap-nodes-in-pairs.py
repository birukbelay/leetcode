# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        if not head or  not head.next:
            return head
        #swapping
        h1=head
        h2=head.next
        #there is no problem even if h3 is None
        h3=head.next.next
        h2.next=h1
        h1.next=h3
        
        h=h2
        while h1.next and h1.next.next:
            prev=h1
            #moving forward
            h1=h1.next
            h2=h1.next
            h3=h1.next.next
            
            h2.next=h1
            h1.next=h3
            prev.next=h2
        return h
        
        
        
        