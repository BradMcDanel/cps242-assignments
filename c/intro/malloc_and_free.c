#include <stdlib.h>

int main(void) {
    // dynamic allocation
    int *a = malloc(10 * sizeof(int));

    // do something with a

    // free the memory
    free(a);
}
