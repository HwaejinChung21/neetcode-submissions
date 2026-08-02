# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, l1, l2):
            newList = ListNode(None)
            dummy = newList

            while l1 and l2:
                if l1.val < l2.val:
                    l1Next = l1.next
                    newList.next = l1
                    l1 = l1Next

                else:
                    l2Next = l2.next
                    newList.next = l2
                    l2 = l2Next
                
                newList = newList.next
            
            if l1:
                newList.next = l1
            
            elif l2:
                newList.next = l2

            return dummy.next
        
        