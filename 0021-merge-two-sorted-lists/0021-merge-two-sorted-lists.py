# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        temp=list3
        arr=[]
        if not list1:
            return list2
        if not list2:
            return list1
        if list1 and list1.val>list2.val:
            list3.val=list2.val
            list2=list2.next
        else:
            list3.val=list1.val
            list1=list1.next
        # print(list3)
        while list1 and list2:
            
            if list1.val<list2.val:
                # arr.append(list1.val)
                list3.next=ListNode(list1.val)
                #                 updating the index
                list3=list3.next          
                
                list1=list1.next
                
            else:
                list3.next=ListNode(list2.val)
                list3=list3.next
                # arr.append(list2.val)
                list2=list2.next
                
                # print("lst2=", list2)
                # print("list3------=", list3)
        # print("slt3", list3, "arr---", arr)
        # for i in arr:
        #     list3.next=ListNode(i)
        #     list3=list3.next
        if list1:
            list3.next=list1
        else:
            list3.next=list2


        return temp
