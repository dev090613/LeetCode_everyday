# 예시
    # my_linked_list.middleNode([1, 2, 3, 4, 5]) => [3]
    # my_linked_list.middleNode([1, 2, 3, 4]) => [3]. middle node가 둘 인 경우 두 번째 것 반환
    # my_linked_list.middleNode([1]) => [1]
# my_linked_list.middleNode([]) => []
# step by step: slow and fast
    # slow pointer와 fast pointer를 준비한다.
    # fast는 말단, slow는 중간 노드를 반환할 것이기 때문에 이 둘은 2배수의 관계이다.
    # slow pointer가 1칸 이동할 때 fast pointer는 2칸 이동한다.
        # fast, slow
        # 1      1(head)
        # 2      3
        # 3      5
        # 4      7
        # 5      9
# O(N), O(1) / 7% 5%
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# 방법2: loop