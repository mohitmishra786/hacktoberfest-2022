/*
This is a Insertion Sort Program written in C++
Worst Time Complexity O(n^2), Space Complexity O(1)
Insertion Sort is Inplace and Stable Sorting Algorithm
The best case time complexity of Insertion Sort is O(n)

Let's consider an example for insertion Sort
arr = [ 10, 20, 5, 7]
here we divide the array in 2 parts. first is sorted and second is unsorted array
╔═══════════════╦═════════════════╗
║ 0......i-1    ║    i......n-1   ║
╠═══════════════╬═════════════════╣
║ Sorted Array  ║ Unsorted Array  ║
╚═══════════════╩═════════════════╝

Dry run for the given array
╔═══════════════╦═════════════════╗
║ Sorted Array  ║ Unsorted Array  ║
╠═══════════════╬═════════════════╣
║ 10            ║ 20, 5, 7        ║  at starting the size of sorted array is 1, hence it is sorted.
╠═══════════════╬═════════════════╣
║ 10, 20        ║ 5, 7            ║  Here we add 20 to the sorted list at it's correct position
╠═══════════════╬═════════════════╣
║ 5, 10, 20     ║ 7               ║  Added 5 at it's correct position
╠═══════════════╬═════════════════╣
║ 5, 7, 10, 20  ║                 ║  at last we add 7 at its correct position and our whole array is sorted. 
╚═══════════════╩═════════════════╝

*/

#include<bits/stdc++.h>
using namespace std;

//This function is used to print the result
void print(vector<int> arr) {
    for(int it : arr)
        cout<<it<<" ";
}

//This is the insertion sort function. 
void InsertionSort(vector<int> arr) {
    int n = arr.size();

    //As we know that the first element is always sorted. 
    for(int i=1; i<n; i++) {
        int key = arr[i];
        int j=i-1;
        while(j>=0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
    print(arr);
}

// Driver code
int main() {
    
    cout<<"Array before performing Insertion Sort"<<endl;
    vector<int> arr = {10, 20, 5, 7};
    //Print the array vector before performing insertion sort.
    print(arr);
    
    //Calling Insertion sort function and passing the arr vector. 
    cout<<endl<<"Array after performing Insertion Sort"<<endl;
    InsertionSort(arr);
    
}