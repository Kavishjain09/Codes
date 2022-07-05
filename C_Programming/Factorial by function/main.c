#include <stdio.h>
#include <stdlib.h>

int f(int n)
{int i,f=1;
for(i=1;i<=n;i++)
{
 f=f*i;

}
 return f;
}
int main()
{ int num,x;
    printf("Enter the value:");
    scanf("%d",&num);
    x= f(num);
    printf("Factorial is:%d",x);

}
