class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        self.pos[val].add(len(self.nums)-1)
        return len(self.pos[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.pos[val]:
            # 1.Get index of the removed value
            index = self.pos[val].pop()
            # 2. Get the value of the last element
            last = self.nums[-1]
            # 3. swap the last element to the index of removed value (for purpose of remove)
            self.nums[index] = last
            # check if removed item == last item
            if self.pos[last]:
                # update the index of swaped val (previously last item)
                # add current index to the dict(set) => remove previous index(len-1)
                self.pos[last].add(index)
                self.pos[last].discard(len(self.nums)-1)
            self.nums.pop()
            return True
        return False
            

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()