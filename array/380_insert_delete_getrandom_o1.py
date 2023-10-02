from random import choice
class RandomizedSet:
    def __init__(self):
        self.hashMap = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.list.append(val)
        self.hashMap[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False

        idx, lastElement = self.hashMap[val], self.list[-1]
        self.list[idx], self.hashMap[lastElement] = lastElement, idx
        self.list.pop()
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)    
