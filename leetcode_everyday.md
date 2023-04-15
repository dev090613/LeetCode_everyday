### add two integer

~~~python
# Given two integers num1 and num2, return the sum of the two integers.

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        sum = num1 + num2
        return sum
~~~

### Middle of the Linked List(876) 4/15

~~~python
# 해결 방법: Two pointer
# 슬로우와 패스트 두 개의 포인터를 준비한다. fast는 말단, slow는 중간의 값을 반환할 것이기 때문에 둘은 2배수의 관계가 된다. 이것이 성립하기 위해서 slow가 1칸 이동할 때 fast는 2칸 이동할 것이다. 
# fast, slow
# 1      1(head)
# 2      3
# 3      5
# 4      7
# 5      9
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
~~~

