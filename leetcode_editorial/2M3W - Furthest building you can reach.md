## 1642. Furthest building you can reach

### 문제

​	`hieghts`, `bricks`, `ladders`가 주어졌다. integer array `heights`는 빌딩의 높이를 나타낸다. David가 배열을 따라 이동하려고 한다. current building의 높이가 next building의 높이보다 높은 경우 이동에 제약이 없으나, 그렇지 않은 경우 빌딩을 오르기 위해 두 빌딩 높이의 차이만큼의 `bricks` 또는 하나의 `ladders`가 필요하다. David는 어느 index까지 이동할 수 있는가?



### Intuition

- 빌딩을 오르기 위해서 `bricks` 또는 `ladders`가 필요하다. 주인공이 최대한 멀리 이동하기 위해서 두 빌딩의 높이 차이가 큰 경우  `ladders`를 allocate 하는 것이 좋다.
  - 다시 말해, priority가 높은 항목에 대해 `ladders`를 allocate하기 위해 heap을 사용한다.
  - 그러기 위해서 일단 인접한 두 빌딩의 높이 차이를 구한다.
- 배열을 완주할 수 있는지 여부는 판단하기 쉬울 것이다. 하지만 어느 지점까지 이동할 수 있는지를 구하기 위해서는 어떤 방법을 사용해야 할까..
  - 우선적으로 `ladders`를 allocate한 후 이것이 소진된 후에는 1) bricks를 배치하거나 2) 이미 배치된 `ladders`를 `bricks`로 교체한 후 `ladders`를 배치한다. 그러한 판단은 지나간 지점의 높이차 중 가장 작은 값이 현재 맞이한 높이차보다 작은 경우 1) 을 실행한다.

### Algorithms

- 루프를 돌며 인접한 두 빌딩의 높이 차이를 구한다. - `diff`

- minHeap에 `diff`를 넣는다.
- minHeap size가 `ladders`의 개수보다 커지는 경우 `ladders` 대신 `bricks`를 사용해야 한다. 단, `heappop()`을 사용하여 가장 작은 diff에 `ladders`가 아닌  `bricks`를 allocate
- `bricks`가 음수인 경우 그 위치를 반환한다.

~~~python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff <= 0:
                continue
            heapq.heappush(minHeap, diff)
            if ladders >= len(minHeap):
                continue
            bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                return i
        return len(heights) - 1
~~~



### Time complexity: `n O(log n)`

Heap의 경우 inserting과 removing에 각각 `O(log x)`가 필요하다, 이때 x는 heap내 item의 개수이다. 최악의 경우 `n - 1`개의 item이 있을 수 있으므로 `O(log n)`. 정확히는 힙의 size는 최대 ladders의 개수와 같으므로 O(log L)이다, 단 

배열에 있는 items에 대해 heap연산을 수행하며 배열의 items의 개수는 `n`개이다.

따라서 `n * O(log L)` , 최악의 경우 L == n

### Space complexity: `O(n)`

힙은 최대 ladders의 개수 만큼의 item을 넣을 수 있으므로 `O(L)`이다. 최악의 경우 ladders의 개수는 배열의 size와 동일하므로 `O(n)`



---

Further, Binary search solution도 공부해보자