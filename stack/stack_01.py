# Stack Implementation using List/Array

class Stack(object):
    def __init__(self,mem=5):
        self.container=[]
        self.mem=mem

    def push(self,item):
        if self.overflow():
            raise Exception("Allocated Memory Full")
        self.container.append(item)

    def pop(self):
        if self.underflow():
            raise Exception("Nothing to Pop")
        return self.container.pop()

    def peek(self):
        if self.underflow():
            raise Exception("Nothing to Show")
        return self.container[-1]

    def underflow(self):
        return len(self.container)==0

    def overflow(self):
        return len(self.container)==self.mem