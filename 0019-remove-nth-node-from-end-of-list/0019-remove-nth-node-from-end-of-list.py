# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# fast와 slow 포인터를 준비한다. 각각은 head에 위치한다.
# n이 주어졌을 때 말단에서 nth 노드를 반환해야 한다.
# (예를 들어, 1이 주어진 경우 마지막 노드를, 2가 주어진 경우 그 이전 노드를 반환한다.)
# 일단 fast를 n칸 보낸다. 그렇다면 slow는 fast에서 (nth)의 이전 노드가 된다.
# 그 다음 fast와 slow를 null까지 보내게 되면 slow의 다음 노드가 remove 될 노드이다.
# 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        # fast를 n칸 보낸다.
        for _ in range(n):
            fast = fast.next
        
        # 예외체리, n이 lengh 이상인 경우
        if fast == None:
            return head.next
        
        # fast와 slow를 마지막 노드까지 보낸다. "while fast:" 가 아님에 주의
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        
# Follow up: Could you do this in one pass?
        