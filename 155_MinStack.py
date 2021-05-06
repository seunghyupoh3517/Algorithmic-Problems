# Need to achieve in constant time
class MinStack(object):
    """
         push  pop  top (first in last out) getMin
    list O(1)  O(1) O(1) - index look up     O(n) 
    
    -> if I can keep track of minimum element and locate it on the top of the stack,
     when pushing the value into the stack then I think I can achieve O(1) as well
    """

    # initalize stack
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            # tuple: (value, minimum value)
            self.stack.append((val,val))
            # without else:, return
        else:
            curr_min = self.stack[-1][1]
            minimum = min(curr_min, val)
            self.stack.append((val, minimum))

    # pop, top, getMin operations will always be called on non-empty stack
    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        # using min(stack) will take O(N) so instead track the min value in push 
        # so that I can simply return the minimum value here at getMin
        return self.stack[-1][1]


