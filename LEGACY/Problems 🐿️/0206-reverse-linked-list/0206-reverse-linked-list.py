# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        None head -> head.next -> ... -> None
        임의의 위치(curr)에서 시작
        3 pointer: prev, curr, next_node
        """
        def reverse(curr, prev):
            # Empty list
            if not curr: 
                return prev
            
            next_node = curr.next
            curr.next = prev
            return reverse(next_node, curr)
                
        return reverse(head, None)