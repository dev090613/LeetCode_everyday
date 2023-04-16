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

### Linked List Cycle(141) 4/16

~~~html
two pointers: Floyd's Tortoise and hare algorithm(플로이드의 토끼와 거북이 알고리듬)

slow runner와 fast runner 둘을 준비한다.
slow runner가 한 칸 이동할 때 fast runner는 두 칸 이동한다
linked list가 cycle이 아닌 경우 fast 또는 fast.next가 null을 만나게 될 것이다.(Flase 반환)
linked list가 cycle인 경우 fast가 slow와 만나게 될 것이다 (True 반환)
~~~

~~~python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: 
                return Trues
        return False
      
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# The space complexity can be reduced to O(1) by considering two pointers at different speed We only use two nodes (slow and fast) so the space complexity is O(1)
~~~

~~~html
Hash_set

linked list를 돌면서 각 노드를 hash_set에 집어넣는다.
만약 
~~~

~~~python
~~~



### Check if Number Has Equal Digit Count and Digit Value(2283) 4/16

~~~python
~~~

