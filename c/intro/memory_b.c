#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    // stack allocation
    int stack_arr[10] = {0};

    // heap allocation
    int n = atoi(argv[1]);
    int* heap_arr = malloc(n * sizeof(int));
}
