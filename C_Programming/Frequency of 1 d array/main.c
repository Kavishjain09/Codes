#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,a[50],n,cnt,f,b[50];
    printf("Enter no of variable :");
    scanf("%d",&n);
    printf("Enter the Elements : ");
    for (i=0; i<n; i++)
    {
        scanf("%d",&a[i]);

    }
    int k=0;
    for (i=0; i<n; i++)
    {   cnt=0;
        f=0;
      for(int j=i+1; j<n; j++)
      {
        if(a[i]==a[j])
        {
            cnt++;
        }
        else
          {  continue;
          }
      }
    if(cnt>1)
    {
    printf("\nFrequency of %d is %d",a[i],cnt);
    }
    }
    return 0;
}
