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

### Reverse Linked List II(92) 4/

~~~python
~~~

### Valid Palindrome(125) 4/21

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

### Reorder Data in Log Files(937) 4/21

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

### Most Common Word(819) 4/22

collections.counter()

~~~python
https://www.geeksforgeeks.org/counters-in-python-set-1/
https://www.geeksforgeeks.org/counters-in-python-set-2-accessing-counters/

# A Counter is a subclass of dict. Therefore it is an unordered collection where elements and their respective count are stored as a dictionary. 

# Example of each type of counter initialization : 

## A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C'])) # Counter({'B': 5, 'A': 3, 'C': 2})

# with dictionary
print(Counter({'A':3, 'B':5, 'C':2})) # Counter({'B': 5, 'A': 3, 'C': 2})

# with keyword arguments
print(Counter(A=3, B=5, C=2)) # Counter({'B': 5, 'A': 3, 'C': 2})
~~~

most_common()

~~~python
# Python example to demonstrate most_elements() on
# Counter
from collections import Counter

coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)

# This prints 3 most frequent characters
for letter, count in coun.most_common(3):
	print('%s: %d' % (letter, count))
~~~

most_common_word

~~~python
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # input: phragraph, ""
        # split(), lower(), re.sub(), not in banned, []
        # collections.counter(), most_common()
        # ouput: most frequent word, not banned ""
        
        my_word = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned] # ' '가 아닌 ''로 받으면 space가 전부 붙어버린다.
        print(f"type of my_word is {type(my_word)}")
        my_counter = collections.Counter(my_word)
        print(f"\ntype of my_counter is {type(my_counter)}")
        print(f"\nmy_counter.most_common(3) is {my_counter.most_common(3)})")
        print(f"\nmy_counter.most_common(1)[0] is {my_counter.most_common(1)[0]})")
        print(f"\ntype of my_counter.most_common(1)[0] {type(my_counter.most_common(1)[0])})")
        return my_counter.most_common(1)[0][0].lower() # tuple이므로 key, value를 쓸 수 없고 index로 접근
        
sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
["hit"]))

# type of my_word is <class 'list'>

# type of my_counter is <class 'collections.Counter'>

# my_counter.most_common(3) is [('ball', 2), ('bob', 1), ('a', 1)])

# my_counter.most_common(1)[0] is ('ball', 2))

# type of my_counter.most_common(1)[0] <class 'tuple'>)

# ball
~~~

### Valid Anagram(242) 4/23

~~~python
# initial order does not matter
# frequences does matter
# there are only 26 letters 
# https://www.geeksforgeeks.org/defaultdict-in-python/

# 방법2: index 26
# counter도 사용할 수 있지 않을까..?

# # 방법1: sorted()/ 64% 10%/ 비추천
# comment: sorting is last resort when coding an algorithm.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# #방법2: index26, string.count()/ 100% 95%/ 추천
# # count() method returns an integer that denotes number of times a substring occurs in a given string. 
# # https://www.geeksforgeeks.org/python-string-count-method/
# # It's practically O(1), however, we're using the built in str.count() method, which theoretically is O(n), and since we call it 26 times this solution is O(26*(n+m)). But, python built-in library methods are efficiently coded for speed ups and can generally be used for efficient solutions.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in "abcdefghijklmnopqrstuvwxyz":
            if s.count(char) != t.count(char):
                return False
        return True

# # 방법3: set(), count()/ 93% 32%
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         for char in set(s):
#             if s.count(char) != t.count(char):
#                 return False
#         return True
        
# # 방법4: hash-map, dict.items()/ 60% 58%/ 비추천
# class Solution:
#     def isAnagram(self, s: str, t:str) -> bool:
#         if len(s) != len(t):
#             return False
#         hash_dict = dict() # it means, {}
#         for char in s:
#             if char in hash_dict:
#                 hash_dict[char] += 1
#             else:
#                 hash_dict[char] = 1
#         for char in t:
#             if char in hash_dict:
#                 hash_dict[char] -= 1
#             else:
#                 return False
#         for k,v in hash_dict.items():
#             if v != 0: # is not None과는 다르다. 이유는?
#                 return False
#         return True
                

# # 방법5: collections.defaultdict()
# 추후 공부 필요
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         tracker = collections.defaultdict(int)
#         for x in s: tracker[x] += 1
#         for x in t: tracker[x] -= 1
#         return all(x == 0 for x in tracker.values())

            # Follow up

# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# Answer

# Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.
~~~

Last Stone Weight(1046) 4/24

~~~python

~~~

### Merge Two Sorted Lists(21) 4/24

![image-20230424094533652](/Users/isntsoo/Library/Application Support/typora-user-images/image-20230424094533652.png)

~~~python
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
~~~

### Contains Duplicate(217) 4/24

~~~python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 방법1: set()과 list()의 크기 차이를 이용
        if len(nums) != len(set(nums)):
            return True
        return False
~~~

Binary Search(704)

~~~python
# #방법1: for i in range(len(arr)) 69%, 96%
# 이 조건에 충족하지 않는 것 같다(You must write an algorithm with O(log n) runtime complexity.)
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # ascending order로 정렬된 arr(nums)
#         # nums 중에서 target을 찾고, 그것의 index를 반환하라
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1

# 방법2: binary search 94%, 96% O(log n) O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 전제: 오름차순 정렬된 arr nums
        # left와 right는 arr의 양 끝 인덱스
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
~~~

4/24

~~~python
def maxSubArray(self, nums: List[int]) -> int:        
	newNum = maxTotal = nums[0]        
	
	for i in range(1, len(nums)):
		newNum = max(nums[i], nums[i] + newNum)
		maxTotal = max(newNum, maxTotal)

	return maxTotal	

def maxSubArray(self, nums: List[int]) -> int:
    maxTotal = temp = nums[0]
    for item in nums[1:]:
        temp = max(item, item + temp)
        maxTotal = max(maxTotal, temp)

    return maxTotal
~~~



### Group Anagrams(49)

~~~python
~~~

