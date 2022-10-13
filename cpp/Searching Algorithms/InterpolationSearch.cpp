#include<iostream>
using namespace std;
int interpolationSearch(int arr[], int start, int end, int key) {
   int dist, valRange, indexRange, est;
   float fraction;

   while(start <= end && key >= arr[start] && key <= arr[end]) {
      dist = key - arr[start];
      valRange = arr[end] - arr[start]; //range of value
      fraction = dist / valRange;
      indexRange = end - start;
      est = start + (fraction * indexRange); //estimated position of the key

      if(arr[est] == key)
         return est;
      if(arr[est] < key)
         start = est +1;
      else
         end = est - 1;
   }
   return -1;
}

int main() {
   int n, searchKey, loc;
   cout << "Enter number of numbers: ";
   cin >> n;
   int arr[n]; //create an array of size n
   cout << "Enter Numbers: " << endl;

   for(int i = 0; i< n; i++) {
      cin >> arr[i];
   }

   cout << "Enter number to search in the list: ";
   cin >> searchKey;

   if((loc = interpolationSearch(arr, 0, n-1, searchKey)) >= 0)
      cout << "Number found at location: " << loc << endl;
   else
      cout << "Number is not found in the list." << endl;
}
