#include <stdio.h>
#include <math.h>

int main()
{
    long long num1 = 1;
    long long num2 = 1;

    int counter = 2;

    while (1)
    {
        long long new_num = num1 + num2;
        num1 = num2;
        num2 = new_num;
        counter += 1;
        printf("\nThe %d number in the sequence is: %d", counter, new_num);
    }
}