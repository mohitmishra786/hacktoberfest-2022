#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
using namespace std;

long long int calculate(vector<long long int> &v, long long int k){
    int count = 0;
}

int main() {

    long long int n,k;
    cin>>n>>k;

    vector<long long int> ans;
    for(int i=0; i<n; i++){
        long long int temp;
        cin>>temp;
        ans.push_back(temp);
    }

    cout<<calculate(ans, k);

    return 0;
}