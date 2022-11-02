class CustomStack:

    def __init__(self, maxSize: int):
        self.size=maxSize
        self.stack=[]

    def push(self, x: int) -> None:
        if len(self.stack)< self.size:
            self.stack.append(x)
        

    def pop(self) -> int:
        return -1 if not self.stack else self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        m= min(k, len(self.stack))
        for i in range(m):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)