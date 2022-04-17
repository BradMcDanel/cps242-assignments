#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  float stack_arr[100];
  float *heap_arr = malloc(100 * sizeof(float));
  for (int i = 0; i < 100; i++) {
    stack_arr[i] = i;
    heap_arr[i] = i;
  }
  float stack_acc = 0;
  float heap_acc = 0;
  for (int i = 0; i < 100; i++) {
    stack_acc += stack_arr[i];
    heap_acc += heap_arr[i];
  }
  printf("%f %f\n", stack_acc, heap_acc);
  return 0;
}
