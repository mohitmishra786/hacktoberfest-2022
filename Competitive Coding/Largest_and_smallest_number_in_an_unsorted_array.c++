#include<iostream>
#include<algorithm>
using namespace std;

pair<int,int> largest_and_smallest_number_in_an_array(int arr[],int size){
    int largest_number = INT_MIN;
    int smallest_number = INT_MAX;

    for(int i = 0; i<size; i++){
        largest_number = max(largest_number, arr[i]);
        smallest_number = min(smallest_number, arr[i]);
    }

    pair<int,int> answer = {largest_number,smallest_number};
    return answer;
}

int main(){
    int arr[] = {10, 14, 28, 11, 7, 16, 30, 50, 25, 18};
    int size = sizeof(arr) / sizeof(arr[0]);
    pair<int,int> p = largest_and_smallest_number_in_an_array(arr, size);
    cout << p.first << " " << p.second << '\n';
}