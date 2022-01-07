# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import choice

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.__nums = []
        while head:
            self.__nums.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.__nums)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()