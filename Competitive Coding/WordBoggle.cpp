#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
   
    bool dfs(vector<vector<pair<int,int>>>&v, vector<vector<int>>&vis, string s,int i,int x,int y)
    {
        if(i>=s.length()) return true;
        for(auto j:v[s[i]-'a'])
        {
            bool a;
            if((i==0|| abs(x-j.first)<=1 && abs(y-j.second)<=1))
            {
              if(dfs(v,vis,s,i+1,j.first,j.second));
              return true;
             }         
        }
       return false;   
    }                    
    

vector<string> wordBoggle(vector<vector<char> >& b, vector<string>& d) {
vector<vector<pair<int,int>>> v(25);
vector<vector<int>> vis(b.size(), vector<int>(b[0].size(),0));
vector<string> res;
    for(int i=0;i<b.size();i++){
        for(auto j=0;j<b[0].size();j++){
            v[b[i][j]-'a'].push_back({i,j});
        }
    }

    for(auto i:d){
     if(dfs(v,vis,i,0,0,0))res.push_back(i);
    }

    sort(res.begin(),res.end());
    return res;
 }
};


int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<string> dictionary;
        for (int i = 0; i < N; ++i) {
            string s;
            cin >> s;
            dictionary.push_back(s);
        }
       

        int R, C;
        cin >> R >> C;
        vector<vector<char> > board(R);

        for (int i = 0; i < R; i++) {
            board[i].resize(C);
            for (int j = 0; j < C; j++) cin >> board[i][j];
        }

        Solution obj;
        vector<string> output = obj.wordBoggle(board, dictionary);
        if (output.size() == 0)
            cout << "-1";
        else {
            sort(output.begin(), output.end());
            for (int i = 0; i < output.size(); i++) cout << output[i] << " ";
        }
        cout << endl;
    }
}
