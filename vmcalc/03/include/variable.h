#ifndef _VARIABLE_H_
#define _VARIABLE_H_

#include "value.h"

typedef struct {
  char* name;
  int value;
} Variable;

int get_variable_index(char** variable_names, uint8_t* n, char* name);
void set_variable(Variable* variables,
                  uint8_t* variable_length,
                  char* name,
                  Value *value);
Value get_variable(Variable* variables, uint8_t variable_length, char* name);
Value extract_value(Variable* variables, Value* value);


#endif // _VARIABLE_H_