#ifndef _IO_H_
#define _IO_H_

#include <stdbool.h>

char* read_file(char* filename);
char* next_word(char** str);
bool is_number(char* str);
bool is_alphanumeric(char* str);

#endif // _IO_H_