# coding=utf-8

"""
    question url: https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = set()
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.randomSet.add(val)
        if len(self.randomSet) == self.length:
            return False
        self.length += 1
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        self.randomSet.discard(val)
        if len(self.randomSet) == self.length:
            return False
        self.length -= 1
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randomIndex = random.randint(0, self.length-1)
        return list(self.randomSet)[randomIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()