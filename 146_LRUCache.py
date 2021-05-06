class DoubleLinkedNode(object):
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache(object):
    # Achieve get and put with O(1) time complexity without using the Orderedict class function 
    # - OrderedDicct structure is actually combines behind both hashmap and linked list
    # O(capacity) Space - space is used only for a hashmap, double linked list with at most (capacity + 1 elements)
    """
    class LRUCache(OrderedDict):
        def get(self, key):
            if key not in self:
                return -1
            self.move_to_end(key)
            return self[key]

        def put(self, key, value):
            if key in self:
                self.move_to_end(key)
            self[key] = value
            if len(self) > self.capacity:
                self.popitem(last = False)
    """

    """
        Constant time complexity of get, put can think of is hashmap - key lookup, append => Hashmap
        In order to acheive least recently used cache - need to keep track of the orders, what has been used .. => Double linked list in constant time, pointers
        Then "Head, Tail" nodes to point the nodes and indicate the order - whenever the node accessed move to head - change the pointer
        Will always have head, tail nodes and will insert nodes in between head and tail 
        Combined datastructure :: A cache contains double linked node
        i.e. head <-> key1:val1 <-> key2:val2 <-> ... <-> key n:val n <-> tail

        With the double linkd list node class, need more functions to achieve LRU features
        <PUT>
            - Add node: always add new node to head
            - Move to head node: update the value, then update head pointer
            - Remove tail node: when the capacity exceeds and return the value 
                - need to keep track of the size of the cache, need new variable

        <GET>
           - Return the value and need to update the node to head pointer
    """
    def add_node(self, node):
        # update pointers of adding node
        # Head <- Node -> X
        #         <->
        node.prev = self.head
        node.next = self.head.next
        # update pointers of head node
        self.head.next.prev = node
        self.head.next = node
        
        self.size += 1
        
    def remove_node(self,node):
        #   <- node -> 
        prev = node.prev
        new  = node.next
        
        prev.next = new
        new.prev = prev
        
        self.size -= 1

    def move_to_head(self, node):
        # detach the current pointers -> remove-node
        self.remove_node(node)
        # attach the pointers to head and what head was pointing -> add_node
        self.add_node(node)
        
    def pop_tail(self):
        end = self.tail.prev
        self.remove_node(end)
        return end # so that I can remove the end from the dictionary
        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key, None)
        if node:
            node.value = value
            self.move_to_head(node)
        else:
            # if the node doesn't exist, create new node    
            new = DoubleLinkedNode()
            new.key = key
            new.value = value
            
            if self.size >= self.capacity:
                end = self.pop_tail()
                del self.cache[end.key]
            
            self.cache[key] = new
            self.add_node(new)


if __name__ == '__main__':
    input = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
