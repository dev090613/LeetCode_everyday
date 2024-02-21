## 2.19(월) 231.  Power of Two

- 거듭제곱을 비트로 표현하였을 때의 규칙성을 배울 수 있다. 관련된 개념으로, integer 최대값 및 최소값, 그리고 오버플로우에 대해서 생각해볼 수 있다.

#### 문제

주어진 integer n에 대하여, n이 2의 거듭제곱인지 Boolean을 판단하라

<u>follow-up: loop와 recursion을 사용하지 않고 판단할 수 있는가</u>

#### Intuition - Bitwise

- 

 ~~~python
 
 ~~~

#### Complexity



> 컴퓨터에서의 수표현
>
> https://namu.wiki/w/%EC%BB%B4%ED%93%A8%ED%84%B0%EC%97%90%EC%84%9C%EC%9D%98%20%EC%88%98%20%ED%91%9C%ED%98%84
>
> 오버플로
>
> https://namu.wiki/w/%EC%98%A4%EB%B2%84%ED%94%8C%EB%A1%9C

## 2월 20일(화) 268. Missing number

문제

Intuition

Complexity

~~~python
~~~

## 2월 21일(수) 201.  Bitwise AND of numbers range

#### 문제

Integers `left`, `right`가 주어졌을 때, `[left, right]`에 해당하는 integers에 대하여 bitwise AND operation을 한 경우 result를 구하라

#### Intuition

`right`의 maximum value가 상당히 크므로(2^31 - 1) O(n) time 보다 효율적이어야 한다.

~~~python
~~~

#### Complexity

## 2월 21일(수) 1272. Remove Interval

#### Intuition

- 제거해야 할 부분은 기준으로, 이 부분과 겹치지 않는 부분을 `append()`한다

~~~python
# 코딩 스타일이 좋다
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        ta, tb = toBeRemoved
        for a, b in intervals:
            if (t:= min(b, ta)) > a:
                ans.append([a, t])
            if (t:= max(a, tb)) < b:
                ans.append([t, b])
        return ans
~~~

#### Complexity

- Time: `O(n)`, input array를 scan한다.
- Space: `O(1)`, Output 이외의 공간은 별도로 할당하지 않는다.
