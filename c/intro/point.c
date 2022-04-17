#include <stdio.h>

typedef struct Point {
    int x;
    int y;
} Point;

void print_point(Point p) {
    printf("(%d, %d)\n", p.x, p.y);
}

int main(void) {
    Point p;
    p.x = 1;
    p.y = 2;
    print_point(p);
    return 0;
}
