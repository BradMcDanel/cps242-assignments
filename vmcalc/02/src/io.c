#include "io.h"
#include <stdio.h>
#include <stdlib.h>

#define MAX_LENGTH 128

static void skip_space(char **str) {
  while (**str == ' ' || **str == '\t' || **str == '\n' && **str != '\0') {
    (*str)++;
  }
}

char *read_file(char *filename) {
  FILE *fp = fopen(filename, "r");
  if (fp == NULL) {
    printf("Error opening file\n");
    exit(1);
  }

  fseek(fp, 0, SEEK_END);
  long fsize = ftell(fp);
  fseek(fp, 0, SEEK_SET);

  char *string = malloc(fsize + 1);
  fread(string, fsize, 1, fp);
  fclose(fp);

  string[fsize] = 0;
  return string;
}

char *next_word(char **str) {
  if (**str == '\0') {
    return NULL;
  }

  char *word = malloc(sizeof(char) * MAX_LENGTH);

  if (**str == '(' || **str == ')') {
    word[0] = **str;
    word[1] = '\0';
    (*str)++;
    skip_space(str);
    return word;
  }

  int i = 0;
  while (**str != ' ' && **str != '\t' && **str != '\n' && **str != '\0' &&
         **str != '(' && **str != ')') {
    word[i] = **str;
    i++;
    (*str)++;
  }

  word[i] = '\0';
  skip_space(str);

  return word;
}

bool is_number(char *str) {
  int i = 0;
  while (str[i] != '\0') {
    if (str[i] < '0' || str[i] > '9') {
      return false;
    }
    i++;
  }
  return true;
}

bool str_equals(char *str1, char *str2) {
  int i = 0;
  while (str1[i] != '\0' && str2[i] != '\0') {
    if (str1[i] != str2[i]) {
      return false;
    }
    i++;
  }

  if (str1[i] != str2[i]) {
    return false;
  }

  return true;
}

bool is_variable(char *str) {
  // must start with a letter a-z or A-Z
  if ((str[0] < 'a' || str[0] > 'z') && (str[0] < 'A' || str[0] > 'Z') ||
      str[0] == '_') {
    return false;
  }

  int i = 1;
  while (str[i] != '\0') {
    if ((str[i] < 'a' || str[i] > 'z') && (str[i] < 'A' || str[i] > 'Z') &&
        (str[i] < '0' || str[i] > '9') && (str[i] != '_')) {
      return false;
    }
    i++;
  }
  return true;
}
