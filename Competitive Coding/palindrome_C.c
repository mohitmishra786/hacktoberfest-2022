/* Program to check if the string is palindrome or not*/

#include <stdio.h>
#include <string.h>

// Defining a MAX length for the string as 100
#define MAX 100

int isPalindrome(char *str, int length)
{
    /*
     * Function that checks if a given string is a palindrome or not
     * input : string, length of the string
     * output : 1 if palindrome, 0 if not
     */
    for (int i = 0; i < length / 2; i++)
    {
        // Check if the character at ith index is same as the character at (length - i - 1)th index
        if (str[i] != str[length - i - 1])
        {
            // If not, return 0
            return 0;
        }
        // If yes, return 1
        return 1;
    }
}

int main()
{
    char str[MAX];
    printf("Enter a string: ");
    // Taking Input from the user
    scanf("%s", str);
    // String Length
    int length = strlen(str);
    if (isPalindrome(str, length))
    {
        printf("The string is a palindrome");
    }
    else
    {
        printf("The string is not a palindrome");
    }
    return 0;
}