#include <stdio.h>
#include "libcheckprime.h"

void main()
{
    while (1)
    {
        int n;
        printf("\nInput integer (0: exit) => ");
        scanf("%d", &n);
        if (n == 0) break;
    if (checkprime(n) == n)
            printf("%d is a prime Num \n", n);
        else
        printf("%d is not a prime Num \n", n);
    }
}