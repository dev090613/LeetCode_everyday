# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 방법1: recursive approch/ O(n+m) O(n+m)/ 
        # 전제: l1와 l2는 정렬된 list
        # 점화식은 위의 사진과 같다. mergedList가 포인트.
        
        # corner case: l1와 l2 중 하나가 null 인 경우 나머지 list의 헤드를 반환하면 merge가 완성된다.
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        # 점화식 구현: 비교대상 이후의 노드들은 이미 merged 되었다고 가정
        elif list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else: 
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        