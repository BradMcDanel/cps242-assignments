#ifndef _VALUE_H_
#define _VALUE_H_

typedef enum ValueType {
  VT_NIL = 1,
  VT_VALUE = 2,
  VT_VARIABLE = 3,
} ValueType;

typedef struct {
  ValueType type;
  int value;
} Value;

#endif // _VALUE_H