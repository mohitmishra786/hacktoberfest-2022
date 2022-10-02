/*
Iterative Quicksort algorithm (in C++)
*/

#include <bits/stdc++.h>
using namespace std;

//an utility function to swap values of two integer variables
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

//this function implements the partioning algorithm
/*
it takes the last element as the pivot
places the pivot at its correct position in the sorted array
places all the elements smaller or equal to the pivot to its left
places all the elements greater than the pivot to its right
and returns the obtained index of the pivot element

PARAMETERS:
arr -> the array in consideration
l, r -> starting and ending indices (respectively) of the array in consideration
*/
int partition(int arr[], int l, int r){
    int p = arr[r]; //taking the last element as the pivot

    int i = l-1; //partioning index

    int j;//loop variable
    for (j=l; j<r; j++){
        if (arr[j]<=p){
            i++;
            swap(&arr[i],&arr[j]);
        }
    }
    swap(&arr[++i], &arr[r]);

    return i;
}

//function to implement the iterative quicksort algorithm
/*
PARAMETERS:
arr -> array to be sorted
l, r -> starting and ending indices (respectively) of the part of the array in consideration
*/
void quicksort_iterative(int arr[], int l, int r){
    
    //auxiliary stack
    int stack[r-l+1];

    //initializing top index of the stack
    int top_ind = -1;

    //pushing intial values of l and r to the stack
    stack[++top_ind] = l;
    stack[++top_ind] = r;

    //while stack is not empty...
    while(top_ind>=0){
        //pop values of l and r
        r = stack[top_ind--];
        l = stack[top_ind--];

        //index of the pivot element through partitioning algorithm
        int p = partition(arr, l, r);

        //if there are elements between l and p, then
        //push the left part of the array to the stack
        if(p-1>l){
            stack[++top_ind] = l;
            stack[++top_ind] = p-1;
        }

        //if there are elements between p and r, then
        //push the right part of the array to the stack
        if(p+1<r){
            stack[++top_ind] = p+1;
            stack[++top_ind] = r;
        }

    }
}

//this functions prints the elements of the array
/*
PARAMETERS:
arr -> the array, whose elements are to be printed
n -> the length of the array
*/
void print_arr(int arr[], int n){
    int i; //loop variable
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
}


int main(){
    int i; //loop variable
    int n; //length of the array

    cout<<"Enter the length of the array: ";
    cin>>n;

    int arr[n];
    cout<<"Now, enter "<<n<<" space-separated integers corresponding to the elements of the array:- \n";
    for(i=0; i<n; i++){
        cin>>arr[i];
    }

    quicksort_iterative(arr,0,n-1); //sorting the array through iterative quicksort

    cout<<"The sorted array is as follows:- \n";
    print_arr(arr, n);

    return 0;
}