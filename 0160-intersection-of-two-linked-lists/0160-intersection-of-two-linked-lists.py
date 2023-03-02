# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1=[]
        list2=[]
        
        
        while headA:
            list1.append(headA)
            headA=headA.next
        while headB:
            list2.append(headB)
            headB=headB.next
            
        l1=len(list1)-1
        l2=len(list2)-1
        
        if list1[l1]!=list2[l2]:
            return None
        while l1>=0 and l2>=0 and list1[l1]==list2[l2]:
            l1-=1
            l2-=1
        return list1[l1+1]
            
        
        
        