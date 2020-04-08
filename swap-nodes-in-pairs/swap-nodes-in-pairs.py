# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        
        node = ListNode(head.next.val)
        temp = head.next
        head.next = self.swapPairs(temp.next)
        node.next = head
        
        return node