from queue import LifoQueue
class MyQueue:

    def __init__(self):
        self.top = -1
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()
        

    def push(self, x: int) -> None:
        # self.top+=1
        self.stack1.put(x)
        

    def pop(self) -> int:
        # self.top-=1
        if not self.stack2.empty():
            return self.stack2.get()
        else :
            while not self.stack1.empty():
                self.stack2.put(self.stack1.get())
            return self.stack2.get()
        

    def peek(self) -> int:
        if not self.stack2.empty():
            top = self.stack2.get()
            self.stack2.put(top)
        else :
            while not self.stack1.empty():
                self.stack2.put(self.stack1.get())
            top = self.stack2.get()
            self.stack2.put(top)
        return top
        

    def empty(self) -> bool:
        if self.stack1.empty() and self.stack2.empty() :
            return True
        else :
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()