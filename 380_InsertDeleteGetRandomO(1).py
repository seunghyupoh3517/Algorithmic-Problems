
"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
 
 
Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

class RandomizedSet(object):
    #          Insert   Remove  getRandom
    # HashMap    O(1)    O(1)     O(n)
    # Array      O(1)    O(n)     O(1)
    
    def __init__(self): #
        self.hashmap = dict()
        self.array = list()
        
        
    def insert(self, val: int): # O(1)
        if val not in self.hashmap:
            # append to array
            self.array.append(val)
            # add the value & index to hashmap
            # key : val & value : index
            self.hashmap[val]=len(self.array)-1
    
    def remove(self, val: int): # O(1)
        if val in self.hashmap:
            lastVal = self.array[-1]
            
            # self.array = [1,2,3,4,5]
            # remove 3 !
            # problem : removal for array O(n) but we want O(1)
            # solution
            # step 1 : switch position of '3' and the very last element
            # a,b = b,a
            # self.array[self.hashmap[3]], self.array[-1] = self.array[-1], self.array[self.hashmap[3]]
            # step 2: pop!
            # self.array.pop() --> 3 was removed!!
            # step 3 : update the change in hashmap as well
            # self.hashmap
            self.hashmap[lastVal], self.hashmap[val] = self.hashmap[val], self.hashmap[lastVal]
            del self.hashmap[val]
        
        
    def getRandom(self): # O(1)
        #random.random(0, n) --> 3
        #random.choice(list)
        randInt = x
        return self.array[randInt]
    # list(dictionary) : O(n)
    # 
        
        
## Ordered --> Binary!!!
## 