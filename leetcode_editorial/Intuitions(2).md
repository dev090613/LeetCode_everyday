

## 3.20 Wed - Binary subarray with sum

<img src="/Users/isntsoo/github/LeetCode_everyday/leetcode_editorial/images/image-20240320230603693.png" alt="image-20240320230603693" style="zoom: 50%;" />

#### Intuition

- Sliding window algorithms에 교집합을 접목시킨 문제이다. 
- Two pointer를 사용하였을 때, `goal` 에 도달하였음에도 value가 0인 element가 현재 r 포인터의 오른쪽에 더 존재할 수 있지만 이러한 모든 경우의 수를 고려한 subarray의 개수를 일일이 고려하기 어렵다. 따라서 `goal 이하` 에 도달한 경우와 `goal - 1 이하`에 도달한 경우의 차를 구한다면 `goal`에 도달한 경우의 수만을 구할 수 있다.
- 만약 `goal == 2`인 경우, `goal`이 2, 1, 0인 경우의 subarray 총 합을 구한 후 1, 0인 경우를 빼는 것이다.

![image-20240320230651668](/Users/isntsoo/github/LeetCode_everyday/leetcode_editorial/images/image-20240320230651668.png)

#### Time and Space Complexity

O(n), O(1)



---

3월 25일 월요일 - Find All Duplicates in an array

<img src="/Users/isntsoo/github/LeetCode_everyday/leetcode_editorial/images/image-20240325194935964.png" alt="image-20240325194935964" style="zoom: 50%;" />

Intuition

- 문제점
  - O(n) Time, O(1) Space라는 constrains이 문제를 어렵게 만든다.
  - 처음에 떠올렸던 방법은 토끼와 거북이 알고리즘이었지만 `len(nums)`의 값을 가진 `n` 에 의해 인덱스 에러가 발생하여 포기했다. 그리고  O(n) Space 로 문제를 풀었다. 하지만 제한사항을 지키면서 풀어내고 싶은데 어떻게 가능할까.?

1. [1..n] Array이므로 n - 1을 index로 삼는다. 

2. 순회하면서 Input array에 (-)를 mark한다. 동일한 value일 경우 (-)를 마주치게 될 것이다.