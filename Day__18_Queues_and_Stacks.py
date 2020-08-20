

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        temp = self.stack.pop()
        return(temp)
    
    def dequeueCharacter(self):
        temp1 = self.queue.pop(0)
        return(temp1)

    # Write your code here

