#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c;
    printf("Enter the no.:");
    scanf("%d",&a);


    while (a<100)
    {
        while (a!=1)
        {
            b=a/10;
            c=a%10;
            a=(b*b)+(c*c);
        }

        while (a==1)
        {
            printf("The no. is happy");
        }
        while (a<=9&&a!=1)
        {
            printf("The no. is unhappy");
        }
    }


    return 0;
}
