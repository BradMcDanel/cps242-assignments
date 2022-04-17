#include <stdio.h>
#include <stdlib.h>

#include "io.h"

int main(int argc, char *argv[]) {
  char *filename = argv[1];
  char *str = read_file(filename);
  char *word = next_word(&str);
  while (word != NULL) {
    printf("%s\n", word);
    word = next_word(&str);
  }

  return 0;
}
