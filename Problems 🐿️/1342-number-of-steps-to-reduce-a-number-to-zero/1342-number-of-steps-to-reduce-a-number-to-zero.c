int numberOfSteps(int num)
{
    int step = 0;
    
    while(num)
    {
        step++;
        if(num % 2 == 0)
        {
             num = num >> 1;
        }
        else
            num--;
    }
    return step;
}