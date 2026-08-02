# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur = head
        dummy = head
        prev = None
        newList = None
        tail = None

        while cur:
            count += 1

            if count == k:
                # keep track of next node
                curNext = cur.next
                tempTail = dummy

                for i in range(k):
                    nxt = dummy.next
                    dummy.next = prev
                    prev = dummy
                    dummy = nxt
                
                if tail:
                    tail.next = prev

                if not newList:
                    newList = prev
                
                tempTail.next = curNext
                tail = tempTail

                prev = None
                cur = curNext
                count = 0

            else:
                cur = cur.next

        return newList
        