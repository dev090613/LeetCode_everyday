# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next: # fast가 1칸 이동한 경우는 어차피 필요가 없으니
            fast = fast.next.next
            slow = slow.next
        # while fast:
        #     fast = fast.next
        #     if fast:
        #         fast = fast.next
        #     else: break
        #     slow = slow.next
        return slow