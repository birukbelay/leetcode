class Nod:
    def __init__(self, x):
        self.val = x
        self.next = None
class MyLinkedList:

    def __init__(self):
        
        self.tail = None
        self.size=0
        self.head=None

    def get(self, index: int) -> int:
        if self.size>index and self.head is not None:
            cur=self.head
            for i in range(index):
                cur=cur.next
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Nod(val)
            self.tail = self.head
        else:
            node= Nod(val)
            node.next=self.head
            self.head=node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Nod(val)
            self.tail = self.head 
        else:
            new_node = Nod(val)
            self.tail.next = new_node 
            self.tail = new_node
        self.size += 1
#         cur=self.head
#         if cur:
#             while cur.next:
#                 cur=cur.next
        
#             cur.next=Nod(val)
#         else:
#             self.addAtHead(val)
#         self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size>=index:
            
            if index==0:
                self.addAtHead(val)
                return
            
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            new=Nod(val)
            new.next=cur.next            
            cur.next=new
            if new.next is None:
                self.tail = new
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        # print(index)
        if not self.head or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
                
                
        else:
            cur=self.head
            
            for i in range(index-1):
                if cur.next is None:
                    return
                cur=cur.next
            cur.next=cur.next.next
            if cur.next is None:
            
                self.tail = cur
            self.size-=1
                
#         if self.size>index:
#             cur=self.head
            
#             for i in range(index):
#                 cur=cur.next
#             if cur.next:
#                 cur.val=cur.next.val
#                 cur.next=cur.next.next
#             else:
#                 cur=None
#             self.size-=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)