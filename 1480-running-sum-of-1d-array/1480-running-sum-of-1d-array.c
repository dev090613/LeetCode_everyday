/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    
    int i;
    
    // 반환할 배열(result)을 동적으로 할당(malloc). 할당된 배열의 크기는 주어진 배열(nums)의 크기(numsSize)와 동일
    int* result = (int*)malloc(numsSize*sizeof(int));
    // 누적합 계산을 위해 result[0]을 0으로 초기화
    result[i] = 0;
    result[i] = result[i] + nums[i];
    
    for(i=1; i<numsSize; i++)
    {
        result[i] = result[i-1] + nums[i];
    }
    // 반환할 배열의 크기를 포인터를 사용하여 입력된 변수(returnSize)에 할당
    // 이 코드가 없으면 반환된 배열의 크기를 알 수 없기 때문에 메모리 누수(memory leak)와 같은 문제가 발생
    *returnSize = numsSize;
    
    return result;
}