#include <stdio.h>

int main()
{

    char array_string[256];
    int d;

    printf("Enter a string: ");

    scanf("%s", array_string);

    printf("Printing a string: %s", array_string);

    printf("\n Enter an integer: ");
    scanf("%d", &d);

    printf("\nPrinting an integer: %d", d);

    return 0;
}