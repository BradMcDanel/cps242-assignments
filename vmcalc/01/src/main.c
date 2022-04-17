#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <inttypes.h>

#include "io.h"

#define MAX_PROGRAM_SIZE 2048

typedef enum {
  OP_ADD
} Opcode;

typedef struct {
  uint8_t code[MAX_PROGRAM_SIZE];
} Program;

Program program = {0};
int program_counter = 0;

int main(int argc, char *argv[]) {
  char *filename = argv[1];
  char *str = read_file(filename);
  char *word = next_word(&str);
  while (word != NULL) {
    bool is_num = is_number(word);
    bool is_alphanum = is_alphanumeric(word);
    printf("%s (%d/%d)\n", word, is_num, is_alphanum);
    word = next_word(&str);
  }

  return 0;
}
