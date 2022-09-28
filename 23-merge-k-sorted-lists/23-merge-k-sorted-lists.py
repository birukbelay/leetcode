# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapArr=[]
        
        for nodes in lists:            
            while nodes:
                heapq.heappush(heapArr, nodes.val)
                nodes = nodes.next
        print(heapArr)
        listNode=ListNode()        
        temp=listNode
        while heapArr:
            listNode.next = ListNode(heapq.heappop(heapArr))
            listNode = listNode.next
        return temp.next
            
        