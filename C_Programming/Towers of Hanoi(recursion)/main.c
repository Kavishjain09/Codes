#include <stdio.h>
#include <stdlib.h>

void towerOfHanoi(int n, char x, char z, char y);

int main()
{
int n=3;
towerOfHanoi(n, 'A', 'C', 'B');
return 0;
}
void towerOfHanoi(int n, char x, char z, char y)
{
if (n==1)
 {
  printf("\n Move disk 1 from tower %c to tower %c",x, z);
  return;
 }
  towerOfHanoi(n-1, x, y, z);
  printf("\n Move disk %d from tower %c to tower %c",n, x, z);
  towerOfHanoi(n-1, y, z, x);
}
