#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;


int main() {

    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);

    string a;
    cin>>a;

    map<string,int> ans;

    for(int i = 0; i<a.size(); i++){
        string temp = a.substr(i,a.size()-i);
        ans[temp] = i;
    }

    cout<<ans.size()<<" ";
    for(auto i:ans){
        cout<<i.second<<" ";
    }


    return 0;
}