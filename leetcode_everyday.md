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

### Remove Nth Node From End of List(19) 4/17

~~~html
fast와 slow 포인터를 준비한다. 각각은 head에 위치한다.
n이 주어졌을 때 말단에서 nth 노드를 반환해야 한다.
(예를 들어, 1이 주어진 경우 마지막 노드를, 2가 주어진 경우 그 이전 노드를 반환한다.)
일단 fast를 n칸 보낸다. 그렇다면 slow는 fast에서 (nth)의 이전 노드가 된다.
그 다음 fast와 slow를 null까지 보내게 되면 slow의 다음 노드가 remove 될 노드이다.
~~~

~~~python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast, slow = head, head
        
        # fast를 n칸 보낸다.
        for _ in range(n):
          	# 예외처리, n이 length 보다 큰 경우
          	if fast is None:
              	return head.next
            fast = fast.next
                
        # fast와 slow를 마지막 노드까지 보낸다. "while fast:" 가 아님에 주의
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        
# Follow up: Could you do this in one pass?
~~~

### Reverse Linked List(206) 4/18

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        before = None
        while temp != None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before
      
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
~~~

~~~python
# recursive solution

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # break point
        # if (head == None) or (head.next == None):
        if (not head) or (not head.next):
            return head
        
        reversed_sublist = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_sublist
    
# time complexity: O(n)
# space complexity: O(n)
# Runtime: 30 ms, faster than 94.46% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 20.4 MB, less than 5.97% of Python3 online submissions for Reverse Linked List.
~~~

### Reverse Linked List II(92) 4/19

~~~python
~~~

### Valid Palindrome(125) 4/20

~~~python
# 방법1: list
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [char.lower() for char in s if char.isalnum()]
        while len(s_list) > 1:
            if s_list.pop(0) != s_list.pop():
                return False
        return True
~~~

~~~python
# 방법2: 데크 자료형
~~~

~~~python
# 방법3: slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # important🌹
        
        return s == s[::-1]
~~~

### Reverse String(344) 4/21

~~~python
# 방법1: two pointer swap
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # left와 right는 index의 역할을 할 것
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
~~~

~~~python
# 방법2: pythonic
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()
      
# When anything other than list is used in place of list, then it returns an AttributeError.
~~~

~~~python
# 방법3: slicing
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # slicing은 문자열과 list를 처리하기 아주 좋은 방법이지만(성능도 좋다)
        # return [s::-1] 은 오답으로 처리된다. 그 이유는
        # 공간복잡도를 O(1)으로 제한하기 때문이다.
        # 이것은 s[:] = s[::-1] 으로 제출하면 해결이 된다.
        # The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original.
        s[:] = s[::-1]
        return s[:]
~~~



### Reorder Data in Log Files(937) 4/22

~~~python
# lambda & '+ operator'
# 문자로 구성된 로그가 숫자 로그보다 이전에 오며, 숫자 로그는 입력 순서대로 둔다

#####################################
## .split(), default: space
# string = "one,two,three"
# words = string.split(',')
# print(words) # ['one', 'two', 'three']

# # .isdigit(), checking for digit
# string = '15460'
# print(string.isdigit()) # True

# string = '154ayush60'
# print(string.isdigit()) # False
#####################################


# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # 식별자를 이용해서 문자로그와 숫자로그를 구분한다
        digits_list = []
        letters_list = []
        for log in logs: 
            if log.split()[1].isdigit():
                digits_list.append(log)
            else:
                letters_list.append(log)
        # letters_list.sort(key=lambda x: x.split()[0])
        # letters_list.sort(key=lambda x: x.split()[1:])
        letters_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters_list + digits_list

        
# key 인자에 람다 함수를 전달합니다. 
# 이 람다 함수는 두 개의 키를 가지고 정렬합니다. 
# 첫 번째 키는 로그의 두 번째 단어 이후의 모든 단어를 튜플로 반환합니다. 
# 이를 통해 로그의 두 번째 단어 이후에 오는 모든 단어들을 우선순위에 따라 정렬할 수 있습니다. 
# 두 번째 키는 로그의 첫 번째 단어를 반환합니다. 
# 이를 통해 두 로그의 첫 번째 단어가 같은 경우, 그 뒤의 단어들을 알파벳 순서에 따라 정렬할 수 있습니다.

# sort, sorted
# https://blog.naver.com/PostView.naver?blogId=wideeyed&logNo=221745416992

# lambda
#  letters.sort()에서 key 인자로 사용되는 람다 함수는 로그 파일의 문자 로그를 정렬하는 데 사용됩니다. 이 람다 함수는 sort() 함수가 로그 파일 리스트를 정렬할 때 어떤 기준을 사용해야 하는지를 알려줍니다.

# 람다 함수는 두 개의 키를 가지고 로그 파일 리스트를 정렬합니다. 첫 번째 키는 로그 파일에서 두 번째 단어 이후의 모든 단어를 튜플로 반환합니다. 이 튜플은 이후의 모든 단어들을 우선순위에 따라 정렬하기 위한 것입니다. 그러므로 이 튜플은 로그 파일에서 두 번째 단어 이후의 모든 단어들을 포함합니다. 예를 들어, "abc def ghi"와 "abc def jkl" 두 문자열이 있다면, 두 번째 단어 이후의 모든 단어들을 비교하면 "ghi"와 "jkl"을 비교하게 됩니다.
# 두 번째 키는 로그 파일의 첫 번째 단어를 반환합니다. 이는 첫 번째 단어가 같은 경우, 두 번째 단어 이후의 단어들을 알파벳 순서에 따라 정렬하게 합니다.
# 따라서 람다 함수는 첫 번째 키는 "def ghi"나 "def jkl"과 같은 튜플을 반환하고, 두 번째 키는 "abc"와 같은 문자열을 반환합니다. 이를 sort() 함수의 key 인자로 전달하면, 이 함수는 로그 파일 리스트를 첫 번째 키로 먼저 정렬하고, 그 다음에 두 번째 키로 정렬합니다.
# 결국 이 함수는 문자로 이루어진 로그는 두 번째 단어 이후의 단어들과 첫 번째 단어를 기준으로 정렬하고, 숫자로 이루어진 로그는 그대로 유지하는 기능을 수행합니다.
~~~

