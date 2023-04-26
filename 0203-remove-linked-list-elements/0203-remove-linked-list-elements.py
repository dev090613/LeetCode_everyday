# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 방법1: sentinel Node/ O(N), O(1)/ 
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # The things are more complicated when the node or nodes to delete are in the head of linked list. How to deal with that? To reduce the problem to the deletion of middle nodes with the help of sentinel node.
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next