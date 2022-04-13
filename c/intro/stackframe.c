#include <stdio.h>

int expi(int a, int b) {
  printf("called\n");
  if (b == 0) {
    return 1;
    } else {
        return a * expi(a, b - 1);
    }
}
    

int main(void) {
    int a = 4;
    int b = 3;
    int c = expi(a, b);
    printf("%d\n", c);
    return 0;
}
