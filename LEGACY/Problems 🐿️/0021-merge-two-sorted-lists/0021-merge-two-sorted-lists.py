# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        list1: [1,2,4]
                ^
                
        list2: [1,3,4,5,6]
                ^
        Return the head of the merged linked list.
        """
                
        dummy = ListNode() # ListNode{val: 0, next: None}
        tail = dummy
 
        # print(list1) # ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next # Dummy start at None