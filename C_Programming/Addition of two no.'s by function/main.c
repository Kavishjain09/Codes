#include <stdio.h>
#include <stdlib.h>

int add(int a,int b)
{
  int result;
  result=a+b;
  return result;
}
int main()
{ int x,y,r;
 printf("Enter the two no.'s ");
 scanf("%d%d",&x,&y);
    r=add(x,y);
    printf("Addition of two no.'s:%d",r);
}
