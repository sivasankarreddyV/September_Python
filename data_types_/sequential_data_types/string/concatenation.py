#include <stdio.h>
#include <string.h>

int main() {
    char str1[100] = "Hello, ";  // String 1
    char str2[] = "world!";      // String 2

    // Concatenate str2 to the end of str1
    strcat(str1, str2);

    // Print the concatenated string
    printf("Concatenated string: %s\n", str1);

    return 0;
}

