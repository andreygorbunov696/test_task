# Definition for singly-linked list.
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


"""


"""
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode со значением {self.val}"

    

head = ListNode(5)
head.next = ListNode([1,2,4])
head.next.next = ListNode([1,3,4])
head.next.next.next = ListNode('TEST')

print(head)            # ListNode со значением 5
print(head.next)       # ListNode со значением abc
print(head.next.next)  # ListNode со значением 4.815162342

print(head.next.next.next)
"""        
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


         

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1.val)
        print(list2.val)
        print(len(list1.val))
        if list1.val <= list2.val:
            print(True)
        else:
            print(False)
        

sol = Solution()
list1 = ListNode([1,2])
list2 = ListNode([1,3,4])
sol.mergeTwoLists(list1, list2)

