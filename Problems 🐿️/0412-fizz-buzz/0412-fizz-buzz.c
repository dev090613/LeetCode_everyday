/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// Function that generates an array of strings based on the FizzBuzz game up to n.
char ** fizzBuzz(int n, int* returnSize){
    // Set the value of the pointer passed as parameter to n.
    *returnSize = n;    
    
    // Allocate memory for an array of n pointers to char.
    char **answer = (char**)malloc(sizeof(char*) * n);

    // Iterate through numbers from 1 to n.
    for(int i = 0; i < n; i++)
    {
        // Allocate memory for a string of size 9 to hold the current number.
        // 이 코드가 포함되지 않으면 answer[i]는 초기화되지 않고 임의의 메모리 위치를 가리킴. 
        //'sprintf'를 사용하여 이 메모리 위치에 쓰려고 하면 세그먼트 오류 또는 기타 메모리 관련 오류가 발생.
        //가장 긴 출력 문자열인 "FizzBuzz\0"을 유지하기에 충분하기 때문에 길이 9가 선택. 더 적은 메모리를 할당하면 세그먼테이션 오류가 발생할 수 있음
        answer[i] = (char*)malloc(sizeof(char)*9);
        sprintf(answer[i], "%d", i+1);

        if ((i+1) % 3 == 0 && (i+1) % 5 == 0)
            answer[i] = "FizzBuzz";
        else if((i+1) % 3 == 0)
            answer[i] = "Fizz";
        else if((i+1) % 5 == 0)
            answer[i] = "Buzz";
    }
    return answer;
}