#include <stdio.h>
#include <stdlib.h>

int main()
{float q,p,a,d,da,dt,t,to,ta;
    printf(" __________________________________________");
    printf("\n|    ***************Bill***************    |");
    printf("\n|     Quantity sold:");
    scanf("%f",&q);
    printf("\n     Price per item:");
    scanf("%f",&p);
    printf("    _____________________________________");
    a=q*p;
    printf("\n     Amount:%f",a);

    printf("\n\n     Discount(in percent):");
    scanf("%f",&d);
    da=(a*d)/100;
    dt=a-da;
    printf("\n     Discounted total:%f",dt);
    printf("\n\n     tax:");
    scanf("%f",&t);
    printf("    _____________________________________");
    to=(t*dt)/100;
    ta=dt+to;
    printf("\n     Total amount:%f",ta);
    printf(" \n__________________________________________");





    return 0;
}
