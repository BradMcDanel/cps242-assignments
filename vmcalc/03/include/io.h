#ifndef _IO_H_
#define _IO_H_

#include <stdbool.h>

char *read_file(char *filename);
char *next_word(char **str);
bool str_equals(char *str1, char *str2);
int str_in_list(char *str, char **list, int n);
bool is_number(char *str);
bool is_variable(char *str);

#endif // _IO_H_