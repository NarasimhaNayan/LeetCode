from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        self.topp = -1
        self.size = n
        self.stack = [0]*self.size

    def push(self, num: int):
        if self.topp < len(self.stack)-1:
            # break
            self.topp+=1
            self.stack[self.topp] = num

    def pop(self) -> int:
        if self.topp == -1 :
            return -1
        item_del = self.stack[self.topp]
        self.topp-=1
        return item_del

    def top(self) -> int:
        if self.topp == -1 :
            return -1
        return self.stack[self.topp] 

    def isEmpty(self) -> int:
        if self.topp == -1 :
            return 1
        return 0

    def isFull(self) -> int:
        if self.topp == len(self.stack)-1 :
            return 1
        return 0

