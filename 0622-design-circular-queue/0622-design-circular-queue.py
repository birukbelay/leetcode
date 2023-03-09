class Node():    
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next
class MyCircularQueue:

    def __init__(self, k: int):
        self.link=Node()
        self.size=k
        self.head=None
        self.tail=None
        self.ctr=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
            
        if self.isEmpty():
            self.head=Node(value)
            self.tail=self.head
            self.ctr+=1
            
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
            self.ctr+=1
        return True
        
                
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False        
        self.ctr-=1
        if self.ctr==0:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
        return True
            
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        if self.ctr==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.ctr>=self.size:
            return True
        return False
        


        
    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()