#include <stdio.h>
#include <stdlib.h>

int main()
{
    int d1,m1,y1,d2,m2,y2,h1,h2,m11,m22,days;
    printf("Enter the date\n");
    scanf("%d%d%d",&d1,&m1,&y1);

    printf("Enter the date\n");
    scanf("%d%d%d",&d2,&m2,&y2);


    if(y2>y1)
    {
        if(m2>m1)
        {
            if(d2>d1)
            {

                days=(d2-d1)+((m2-m1)*30)+((y2-y1)*360);

            }
            else
            {
                days=(d2-d1)+((m2-m1)*30)+((y2-y1)*360);

            }

        }
        else
        {
            if(d2>d1)
            {

                days=(d2-d1)+((m2-m1)*30)+((y2-y1)*360);

            }
            else
            {
                days=(d2-d1)+((m2-m1)*30)+((y2-y1)*360);

            }



        }
    }



printf("days difference = %d",days);

return 0;
}
