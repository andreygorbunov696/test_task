from typing import List
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None:
            print(current.val)
            #if current.next is not None:
            #    print(True)
            current = current.next
            if current is not None:
                if current.val == current.next.val:
                    print(current.val)
                    # Bypass the next node as it's a duplicate

                    current = current.next
                

                else:

                # Move to the next unique value if no duplicate is found

                    current = current.next
        return head


sol = Solution()
list = [1,1,2,3,4,4,5,4]


head = ListNode(list[0])
tail = head
#print(head)
for i in list[1:]:
   #print(i)
    tail.next = ListNode(i)
    tail = tail.next
"""print()
print(head.next.next.val)


current_node = head
count = 0
while current_node is not None:
        # increase counter by one
        count = count + 1

        # jump to the linked node
        current_node = current_node.next

test = head
while test is not None:
     print(test.val)
     test = test.next
print()"""
sol.deleteDuplicates(head)