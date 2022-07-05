#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
 int c;
 char n;
 printf("\t\t\t\t--------------------------------------------------");
 printf("\n\t\t\t\t************Welcome To My Super Market************");
 printf("\n\t\t\t\t--------------------------------------------------");
 printf("\n\nCustomer Name:");
 scanf("%s",&n);



 printf("\n\t\t\t\t\t#|Here is the list of types of product|#\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t       |          1.Grocery items             3.Clothes section               |\n");
 printf("\t\t       |          2.Dairy products            4.Footwears                     |\n");
 printf("\t\t       |                   To Exit Press any other Key                        |\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t\tPress the correspond key to select the correspond mention product type: ");
 scanf("%d",&c);

if (c==1)
{ int gro;
  system("cls");
 printf("\t\t\t\t--------------------------------------------------");
 printf("\n\t\t\t\t************Welcome To My Super Market************");
 printf("\n\t\t\t\t--------------------------------------------------\n");
printf("\t\t\t\t\t#|Here is the list of Grocery's items|#\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t       |          1.Grains                    6.Sugar                         |\n");
 printf("\t\t       |          2.Rice                      7.Juice                         |\n");
 printf("\t\t       |          3.Biscuits                  8.Pulses                        |\n");
 printf("\t\t       |          4.Spices                    9.Oil                           |\n");
 printf("\t\t       |          5.Salt                     10.Chocolates                    |\n");
 printf("\t\t       |                   To Exit Press any other Key                        |\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t\tPress the correspond key to select the correspond mention product: ");
 scanf("%d",&gro);
 }
 else if (c==2)
 { int dai;
  system("cls");
 printf("\t\t\t\t--------------------------------------------------");
 printf("\n\t\t\t\t************Welcome To My Super Market************");
 printf("\n\t\t\t\t--------------------------------------------------\n");
 printf("\t\t\t\t\t#|Here is the list of Dairy's products|#\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t       |          1.Milk                      4.Curd                          |\n");
 printf("\t\t       |          2.Cheese                    5.Lassi                         |\n");
 printf("\t\t       |          3.Ice cream                 6.Buttermilk                    |\n");
 printf("\t\t       |                   To Exit Press any other Key                        |\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t\tPress the correspond key to select the correspond mention product: ");
 scanf("%d",&dai);
 }
 else if (c==3)
 { int clo;
 system("cls");
 printf("\t\t\t\t--------------------------------------------------");
 printf("\n\t\t\t\t************Welcome To My Super Market************");
 printf("\n\t\t\t\t--------------------------------------------------\n");
 printf("\t\t\t\t\t#|Here is the list of Clothes|#\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t       |          1.Shirt                     4.Saree                         |\n");
 printf("\t\t       |          2.Jeans                     5.kurta                         |\n");
 printf("\t\t       |          3.T-shirt                   6.Suit                          |\n");
 printf("\t\t       |                   To Exit Press any other Key                        |\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t\tPress the correspond key to select the correspond mention Clothes: ");
 scanf("%d",&clo);
 }
 else if(c==4)
 { system("cls");
 int foot;
  printf("\n\t\t\t\t\t#|Here is the list of Footwears|#\n");
  printf("\t\t\t\t--------------------------------------------------");
 printf("\n\t\t\t\t************Welcome To My Super Market************");
 printf("\n\t\t\t\t--------------------------------------------------\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t       |          1.Scandals                  3.Shoes                         |\n");
 printf("\t\t       |          2.Socks                     4.Slippers                      |\n");
 printf("\t\t       |                   To Exit Press any other Key                        |\n");
 printf("\t\t       |                                                                      |\n");
 printf("\t\t\t----------------------------------------------------------------------\n");
 printf("\t\t\tPress the correspond key to select the correspond mention product type: ");
 scanf("%d",&foot);
 }

 else {
printf("\n\t\t\t\t*********************invalid choice*********************");
}


 }


