"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        newList = Node(0)
        dummy = newList
        cur = head

        while cur:
            newNode = Node(cur.val)
            newList.next = newNode
            copy[cur] = newNode
            newList = newList.next
            cur = cur.next

        cur = head

        while cur:
            if cur.random is not None:
                copy[cur].random = copy[cur.random]

            else:
                copy[cur].random = None

            cur = cur.next

        return dummy.next
            

        