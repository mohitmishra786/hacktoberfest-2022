#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const int inf = numeric_limits<int>::max();

ll merge(ll arr[], ll l, ll mid, ll r){
    ll leftSubSize = mid - l + 1;
    ll rightSubSize = r - mid;

    // left and right subarrays
    ll left[leftSubSize + 1] = {0};
    ll right[rightSubSize + 1] = {0};

    // Fill the left array with the sorted left subarray elements
    for (ll i=0; i<leftSubSize; i++){
        left[i] = arr[l + i];
    }

    // Fill the right array with the sorted right subarray elements
    for (ll j=0; j<rightSubSize; j++){
        right[j] = arr[mid + 1 + j];
    }

    left[leftSubSize] = inf;
    right[rightSubSize] = inf;

    // Fill the array with the correct sorted order
    ll i=0, j=0;
    ll count = 0;

    // Merging procedure
    for (ll k=l; k <= r; k++){
        if (left[i] < right[j]){
            arr[k] = left[i];
            i++;
        }
        else{
            arr[k] = right[j];
            j++;
            // Since the left subarray is sorted every element that comes 
            // after ith element in the subarray will form an inversion
            // # of elements which form an inversions is (sizeOfLeftSubarray - i)
            count += leftSubSize - i;
        }
    }
    return count;
   
}


ll mergeSort(ll arr[], ll l, ll r){
    ll inversions = 0;
    if (l < r){
        ll mid = (l+r)/2;
        // Sort the left subarray
        inversions += mergeSort(arr, l, mid);
        // Sort the right subarray
        inversions += mergeSort(arr, mid+1, r);
        // Merge two arrays
        inversions += merge(arr, l, mid,  r);
        return inversions;
    }
    return inversions;
}


int main(){
    ll t;
    cin >> t;
    while (t--){
        ll n;
        cin >> n;
        ll a[n+1];
        for (ll i=0; i<n; i++) cin >> a[i];
        
        ll invCount = mergeSort(a, 0, n-1);
        cout << invCount << endl;

    }
    return 0;
}