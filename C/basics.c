/*
* This code will document some differences between c++ and c.
*
* Author: Omar Barazanji
* Date: 5/16/2019
*/

#include <stdio.h>  // vs #include <iostream> from in c++

// function prototypes
int test1(int test_var);
int *test2();
void *print_array(int *array, int size);

// main function
int main() {
  printf("Instead of IOStream in c++, you can use printf in C.\n");
  int test = 0;
  printf("test = %d\n", test);
  test = test1(test);
  printf("After calling test1(test), test = %d\n", test);

  printf("functions that return arrays are pointer type.\n");
  int *array = test2();
  printf("\nvalues in array: \n");
  print_array(array, 2);
  return 0;
}

// functions
int test1(int test_var) {
  test_var += 100;
  return test_var;
}

int *test2() {
  static int arr[2];
  for (int i = 0; i < 2; i++) {
    arr[i] = test1(i);
  }
  return arr;
}

void *print_array(int *array, int size) {
  for (int i = 0; i < size; i++) {
    printf("%d\n", array[i]);
  }
}
