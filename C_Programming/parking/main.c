#include <stdio.h>
#include <stdlib.h>

int main()
{
    int d1,m1,y1,d2,m2,y2,days;
    printf("Enter the date\n");
    scanf("%d%d%d",&d1,&m1,&y1);

    printf("Enter the date\n");
    scanf("%d%d%d",&d2,&m2,&y2);

    if(y1<y2)
    {
        if(m1<m2)
        {
            y1++;
            //m1++;
            if(d2>d1)
            {
                days=(d2-d1)+(((12-m1)+m2)*30)+(y2-y1)*360;
            }
            else
            {
                days=(d1-d2)+(((12-m1)+m2)*30)+(y2-y1)*360;

            }
        }
        else if(m2<m1)
        {
            y1++;
            //m2++;
            //days=((30-d2)+d1)+(((12-m2)+m1)*30)+((y2-y1)*360);
            if(d2>d1)
            {
                days=(d2-d1)+(((12-m1)+m2)*30)+(y2-y1)*360;
            }
            else
            {
                days=(d1-d2)+(((12-m1)+m2)*30)+(y2-y1)*360;

            }
        }

        else if(m1==m2)
        {
            if(d1>d2)
            {
                days=(d1-d2)+((y2-y1)*360);
            }
            else

            {
                days=(d2-d1)+((y2-y1)*360);
            }



        }

    }
    printf("days difference = %d",days);

    return 0;
}
