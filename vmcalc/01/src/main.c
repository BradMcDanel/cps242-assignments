#include <stdio.h>
#include <stdlib.h>

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

char *skip_space(char *str) {
  while (*str == ' ' || *str == '\t') {
    str++;
  }
  return str;
}

char *next_word(char *str) {
  if (*str == '\0') {
    return NULL;
  }

  char *word = skip_space(str);
  while (*str != ' ' && *str != '\0' && *str != '\n') {
    str++;
  }

  str++;
  return str;
}

int main(int argc, char *argv[]) {
  char *filename = argv[1];
  char *str = read_file(filename);
  char *word = next_word(str);
  while (*word != '\0') {
    printf("%s\n", word);
    word = next_word(word);
  }
  return 0;
}
