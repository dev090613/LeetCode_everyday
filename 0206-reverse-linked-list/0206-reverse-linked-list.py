# recursive solution

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # break point
        if (not head) or (not head.next):
            return head
        
        result = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return result
    
# time complexity: O(n)
# space complexity: O(n)