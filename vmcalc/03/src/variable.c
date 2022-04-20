#include <inttypes.h>
#include <stdio.h>

#include "variable.h"
#include "value.h"
#include "io.h"

int get_variable_index(char** variable_names, uint8_t* n, char* name) {
  int idx = str_in_list(name, variable_names, *n);
  if (idx == -1) {
    variable_names[*n] = name;
    (*n)++;
    return *n - 1;
  }

  return idx;
}

void set_variable(Variable* variables, uint8_t* variable_length, char* name, Value *value) {
  for (uint8_t i = 0; i < *variable_length; i++) {
    if (str_equals(variables[i].name, name)) {
      variables[i].value = value->value;
      (*variable_length)++;
      return;
    }
  }

  variables[*variable_length].name = name;
  variables[*variable_length].value = value->value;
  (*variable_length)++;
}


Value get_variable(Variable* variables, uint8_t variable_length, char* name) {
  for (uint8_t i = 0; i < variable_length; i++) {
    if (str_equals(variables[i].name, name)) {
      return (Value){.type = VT_VALUE, .value = variables[i].value};
    }
  }
  return (Value) {.type = VT_NIL, .value = 0};
}

Value extract_value(Variable* variables, Value* value) {
  if (value->type == VT_VARIABLE) {
    return (Value){.type = VT_VALUE, .value = variables[value->value].value};
  }
  
  return *value;
}