#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j,k,n;
    printf("Enter the no.\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
    for(j=n-1;j>=i;j--)
    {
    printf(" ");
    }
    for(k=1;k<=i;k++)
    {
    printf("%d",k);
    }
    printf("\n");

    }
    return 0;
}
