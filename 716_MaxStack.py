class MaxStack(object):
    """
          push pop  top                 peekMax popMax
    List  O(1) O(1) O(1) - index lookup O(n)    O(2n) - search the maximum element, remove

    -> if i can keep track of the maximum element when I push element into stack and locate it on
    top of the stack, then I can acheive in O(1) for peekMax, popMax

    | 3,  10 |
    | 10, 10 |
    | 2,   5 |
    | 1,   5 |
    | 5,   5 |
    __________

    """

    def __init__(self):
        self.stack = []

    # keep track of the maximum element on top of the stack
    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
            return
        
        curr_max = self.stack[-1][1]
        maximum = max(curr_max, x)
        self.stack.append((x, maximum))

    # at least one item in stack when below operations - I don't have to check whether the stack empty

    # remove the top value an return
    def pop(self):
        top_val = self.stack[-1][0]
        self.stack.pop()
        return top_val

    # return the top without removal
    def top(self):
        return self.stack[-1][0]

    # return the maximum element without removal
    def peekMax(self):
        return self.stack[-1][1]
    
    # return the maximum element with removal, if there is more than
    # one maximum, remove the top most one 
    ### -> top value is possible not a maximum
    # but since we know what is the maximum value then we can iterate through the stack
    # and if self.stack[i][0] == self.stack[i][1] then that's the maximum value that we need to remove 
    def popMax(self):
        max_val = self.stack[-1][1]
        self.stack.pop()
        return max_val