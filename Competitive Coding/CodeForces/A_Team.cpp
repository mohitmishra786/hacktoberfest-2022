#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
using namespace std;



int main() {

    int n;
    cin>>n;
    vector<vector<int>> v;
    for(int i=0; i<n;i++){
        vector<int> w(3);
        for(int j=0; j<3; j++){
            cin>>w[j];
        }
        v.push_back(w);
    }
    int count = 0;
    for(int i=0;i<n;i++){
        int ct = 0;
        for(int j=0;j<3;j++){
            if(v[i][j] == 1){
                ct++;
            }
        }
        if(ct>=2){
            count++;
        }
    }

    cout<<count;

    return 0;
}