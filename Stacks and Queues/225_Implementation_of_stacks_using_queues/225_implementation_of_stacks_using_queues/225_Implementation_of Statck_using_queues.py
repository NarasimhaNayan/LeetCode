from queue import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        
    def pop(self) -> int:
        # if len(queue1) == 0:
        # q1_size = len(self.queue1)
        
        while len(self.queue1) > 1:
            # print(self.queue1,q1_size)
            self.queue2.append(self.queue1.popleft())
            # q1_size -=1
        ele = self.queue1.popleft()
        self.queue1,self.queue2 = self.queue2,self.queue1
        return ele
         

    def top(self) -> int:
        # q1_size = len(self.queue1)
        res = 0
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
            # q1_size-=1
        if len(self.queue1) == 1 :
            res =self.queue1.popleft()
            self.queue2.append(res)
        self.queue1,self.queue2 = self.queue2,self.queue1
        return res

    def empty(self) -> bool:
        if len(self.queue1) == 0 :
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
        

# Using 1 Queue
from queue import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        for _ in range(len(self.queue1)-1) :
            self.queue1.append(self.queue1.popleft())
        
    def pop(self) -> int:        
        return self.queue1.popleft()
         

    def top(self) -> int:
        return self.queue1[0]
            
        

    def empty(self) -> bool:
        if len(self.queue1) == 0 :
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()