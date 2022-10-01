#include <iostream>
#include <string>
using namespace std;

string longToShort(string s){
    int size = s.size();
    if(size <= 10){
        return s;
    }

    int concat = size - 2;

    string ans = s[0] + to_string(concat) + s[size-1];

    return ans;
    

}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin>>n;

    while(n--){
        string s;
        cin>>s;
        cout<<longToShort(s)<<endl;
    }

    return 0;
}