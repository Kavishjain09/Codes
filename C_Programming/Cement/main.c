#include<stdio.h>
#include<string.h>

struct cm
{
    float a;
    float b;
    float c;
};
int main()

{
    struct cm e[5];
    int i;


    for(i=0; i<5; i++)
    {
        printf("Enter Info of  Cement : %d\n",i+1);

        printf("Percentage of lime and silica:");
        scanf("%f",&e[i].a);
        printf("Percentage of alumina and iron oxide:");
        scanf("%f",&e[i].b);
        printf("Insoluble residue:");
        scanf("%f",&e[i].c);
        printf("\n\n");

    }
    printf("   ***Information Of Grades of cement***");
    for(i=0; i<5; i++)
    {
        printf("\n   Cement: %d",i+1);
        if(e[i].a>=0.66)
        {   if(e[i].a<=1.02)
            {   if(e[i].b>=0.8)
                {   if(e[i].c<=2)
                    {   printf("\nCement grade is OPC 53");
                    }


                }
                else if(e[i].b>=0.66)
                {   if(e[i].c<=4)
                    {   if( e[i].c<=2)
                        {   printf("\nCement grade is OPC 43");

                        }
                        else
                        {   printf("\nCement grade is OPC 33");

                        }
                    }
                    else
                    {   printf("\nCement grade is other than given grades");
                    }
                }
                else
                {   printf("\nCement grade is other than given grades");
                }


            }
            else
            {   printf("\nCement grade is other than given grades");
            }

        }
        else
        {   printf("\nCement grade is other than given grades");
        }

        printf("\n\n");

    }
}
