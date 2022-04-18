#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "io.h"

#define MAX_PROGRAM_SIZE 2048
#define MAX_CONSTANT_SIZE 256
#define MAX_STACK_SIZE 256

typedef enum {
  OP_CONSTANT = 1,
  OP_ADD = 2,
  OP_PRINT = 3,
} OpCode;

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
  Value stack[MAX_STACK_SIZE];
  uint8_t sp;
} VM;

void add_code(Program *program, uint8_t code) {
  program->code[program->code_length] = code;
  program->code_length++;
}

int add_constant(Program *program, Value constant) {
  program->constants[program->constant_length] = constant;
  program->constant_length++;
  return program->constant_length - 1;
}

void print_program(Program *program) {
  printf("===== Program =====\n");
  for (int i = 0; i < program->code_length; i++) {
    printf("[0x%03x] %d\n", i, program->code[i]);
  }
  printf("\n");
  printf("===== Constants =====\n");
  for (int i = 0; i < program->constant_length; i++) {
    printf("%d ", program->constants[i].constant);
  }
  printf("\n");
  printf("===== End =====\n\n");
}

Program generate_program(char *filename) {
  Program program = {0};
  char *str = read_file(filename);
  char *word = next_word(&str);
  while (word != NULL) {
    // I have provided some helper functions to check if a word is:
    //   - a number (e.g. "123")
    //   - a variable (e.g. "_x2321")
    // You can also use str_equals(word, "print") to check if a word is "print"
    bool is_num = is_number(word);
    bool is_var = is_variable(word);
    printf("%s\t(%d/%d)\n", word, is_num, is_var);

    // TODO: Add code to parse OP_CONSTANT, OP_ADD, OP_PRINT instructions.
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
    // TODO: implement a switch statement to handle the different instructions
    switch (code) {
    case OP_CONSTANT: {
      // What do we do here?
      break;
    }
    case OP_ADD: {
      // What do we do here?
      break;
    }
    case OP_PRINT: {
      // What do we do here?
      break;
    }
    }
  }
}

int main(int argc, char *argv[]) {
  char *filename = argv[1];
  Program program = generate_program(filename);
  print_program(&program);
  printf("===== Running =====\n");
  run_program(&program);
  return 0;
}
