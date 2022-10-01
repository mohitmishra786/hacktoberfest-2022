#include<bits/stdc++.h>

using namespace std;

vector<int> wheels;

int count(string s, int m){
    int val = 0;
    for (int i=0; i<m; i++){
        if (s[i] == 'D') val+= 1;
        else val-=1;
    }
    return val;
}

int main(){
    int t; 
    cin >> t;
    while (t--){
        int n; 
        cin >> n;
        wheels.clear();
        wheels.resize(n, 0);
        for (int i=0; i<n; i++){
            cin >> wheels[i];
        }

        for (int j=0; j<n; j++){
            // cout << "HELLO" << endl;
            int m; 
            string s;
            cin >> m >> s;
            int val = count(s, m);
            cout << (20 + val + wheels[j])%10 << " ";
        }
        cout << "\n";
    }
    return 0;
}