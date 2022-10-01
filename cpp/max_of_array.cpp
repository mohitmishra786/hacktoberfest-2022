#include <iostream>
/*
Code author:[Athar Wani] github: @waniathar
Description: This program finds the maximum element in an array.
*/

using std::cin;
using std::cout;
using std::endl;

// function prototyping
int max_of_array(int arr[], int size);
int *read_array(int size);

// main function
int main()
{
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;
    int *arr = read_array(n);
    cout << "The maximum element of the array is: " << max_of_array(arr, n) << endl;
}

// function definition to read the elements of the array
int *read_array(int size)
{
    int *arr = new int[size];
    for (int i = 0; i < size; i++)
    {
        cout<<"Enter the element at index "<<i<<" : ";
        cin >> arr[i];
    }
    return arr;
}

// function definition to find the maximum element of the array
int max_of_array(int arr[], int size)
{
    int max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    return max;
}