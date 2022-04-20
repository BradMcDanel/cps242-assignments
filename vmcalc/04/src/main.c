#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "io.h"
#include "value.h"
#include "variable.h"

#define MAX_PROGRAM_SIZE 2048
#define MAX_CONSTANT_SIZE 256
#define MAX_STACK_SIZE 256
#define MAX_VARIABLE_SIZE 256

typedef enum {
  OP_CONSTANT = 1,
  OP_ADD = 2,
  OP_PRINT = 3,
  OP_VARIABLE = 4,
  OP_ASSIGN = 5,
} OpCode;

typedef struct {
  uint8_t code[MAX_PROGRAM_SIZE];
  int code_length;
  Value constants[MAX_CONSTANT_SIZE];
  int constant_length;
  char* variables[MAX_VARIABLE_SIZE];
  uint8_t variable_length;
} Program;

typedef struct {
  uint16_t pc;
  Value stack[MAX_STACK_SIZE];
  uint8_t sp;
  Variable variables[MAX_VARIABLE_SIZE];
  uint8_t variable_length;
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
    printf("%d ", program->constants[i].value);
  }
  printf("\n");
  printf("===== End =====\n\n");
}

Program generate_program(char *filename) {
  Program program = {0};
  char *str = read_file(filename);
  char *word = next_word(&str);
  while (word != NULL) {
    if (is_number(word)) {
      int constant = atoi(word);
      int constant_idx = add_constant(&program, (Value){.type = VT_VALUE, .value = constant});
      add_code(&program, OP_CONSTANT);
      add_code(&program, constant_idx);
    } else if (str_equals(word, "+")) {
      add_code(&program, OP_ADD);
    } else if (str_equals(word, "print")) {
      add_code(&program, OP_PRINT);
    } else if (str_equals(word, "assign")) {
      add_code(&program, OP_ASSIGN);
    } else if (is_variable(word)) {
      int idx = get_variable_index(program.variables, &program.variable_length, word);
      add_code(&program, OP_VARIABLE);
      add_code(&program, idx);
    }


    // This advances to the next word (don't remove!)
    word = next_word(&str);
  }

  return program;
}

void run_program(Program *program) {
  VM vm = {0};
  for (vm.pc = 0; vm.pc < program->code_length; vm.pc++) {
    // printf("[0x%03x] %d\n", vm.pc, program->code[vm.pc]);
    uint8_t code = program->code[vm.pc];
    switch (code) {
    case OP_CONSTANT: {
      uint8_t constant_idx = program->code[++vm.pc];
      vm.stack[vm.sp++] = program->constants[constant_idx];
      break;
    }
    case OP_ADD: {
      Value v1 = extract_value(vm.variables, &vm.stack[--vm.sp]);
      Value v2 = extract_value(vm.variables, &vm.stack[--vm.sp]);
      Value result = (Value){.type = VT_VALUE, .value = v1.value + v2.value};
      vm.stack[vm.sp++] = result;
      break;
    }
    case OP_PRINT: {
      Value v = extract_value(vm.variables, &vm.stack[--vm.sp]);
      printf("%d\n", v.value);
      break;
    }
    case OP_VARIABLE: {
      uint8_t variable_idx = program->code[++vm.pc];
      vm.stack[vm.sp++] = (Value){.type = VT_VARIABLE, .value = variable_idx};
      break;
    }
    case OP_ASSIGN: {
      uint8_t var_idx = (uint8_t)vm.stack[--vm.sp].value;
      char* name = program->variables[var_idx];
      Value value = vm.stack[--vm.sp];
      set_variable(vm.variables, &vm.variable_length, name, &value);
      break;
    }
    }
  }
}

int main(int argc, char *argv[]) {
  char *filename = argv[1];
  Program program = generate_program(filename);
  print_program(&program);
  run_program(&program);
  return 0;
}
