#include <stdio.h>
#include <stdlib.h>

int *init_array();

int main() {
  int *array = init_array();
  printf("%d\n", array[0]);
  return 0;
}

int *init_array() {
  int *arr_ptr = (int*)malloc(5 * sizeof(int));
  arr_ptr[0] = 1;
  arr_ptr[1] = 2;
  return arr_ptr;
}
