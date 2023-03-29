### add two integer

~~~python
# Given two integers num1 and num2, return the sum of the two integers.

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        sum = num1 + num2
        return sum
~~~

### Running Sum of 1d Array

~~~python
def runningSum(self, nums: List[int]) -> List[int]:
  result = [nums[0]]
  for num in nums[1::]:
    result.append(result[-1] + num)
  return result


def runningSum(self, nums: List[int]) -> List[int]:
    res = [nums[0]]
    for num in nums[1::]:
        res.append(res[-1] + num)
    return res
  
~~~

