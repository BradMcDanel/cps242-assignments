#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "io.h"

#define MAX_PROGRAM_SIZE 2048
#define MAX_CONSTANT_SIZE 256

typedef enum {
  OP_PRINT = 1,
  OP_CONSTANT = 2,
} OpCode;

static char *keywords[] = {
    "print",
    NULL,
};

typedef struct {
  int constant;
} Value;

typedef struct {
  uint8_t code[MAX_PROGRAM_SIZE];
  int code_length;
  Value constants[MAX_CONSTANT_SIZE];
  int constant_length;
} Program;

typedef struct {
  uint16_t pc;

} VM;

void add_code(Program *program, uint8_t code) {
  program->code[program->code_length] = code;
  program->code_length++;
}

Program generate_program(char *filename) {
  Program program = {0};
  char *str = read_file(filename);
  char *word = next_word(&str);
  while (word != NULL) {
    // I have provided some helper functions to check if a word is:
    //   - a number (e.g. "123")
    //   - a variable (e.g. "_x2321")
    //   - a keyword (e.g. "print")
    bool is_num = is_number(word);
    bool is_var = is_variable(word);
    bool is_kw = is_keyword(word, keywords);
    printf("%s\t(%d/%d/%d)\n", word, is_num, is_var, is_kw);

    // TODO: Add OP_PRINT and OP_CONSTANT instructions to the program.
    //     : For OP_CONSTANT, add the constant to the program's constants array.

    // This advances to the next word (don't remove!)
    word = next_word(&str);
  }

  return program;
}

void run_program(Program *program) {
  VM vm = {0};
  for (vm.pc = 0; vm.pc < program->code_length; vm.pc++) {
    uint8_t code = program->code[vm.pc];
    // TODO: implement OP_PRINT and OP_CONSTANT here
  }
}

int main(int argc, char *argv[]) {
  char *filename = argv[1];
  Program program = generate_program(filename);
  run_program(&program);
  return 0;
}
