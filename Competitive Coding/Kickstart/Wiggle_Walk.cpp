#include<bits/stdc++.h>
using namespace std;

pair<int,int> solve(string &v,int R,int C,int rPos,int cPos);
pair<int,int> anotherSolve(string &v, int R, int C, int rPos, int cPos);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t,i;
    cin>>t;
    i=1;

    while(t--){

        int N,R,C,rPos,cPos;

        cin>>N;
        cin>>R>>C>>rPos>>cPos;

        string v;
        cin>>v;


        auto ans = anotherSolve(v, R, C, rPos-1, cPos-1);

        cout<<"Case #"<<i<<": "<<ans.first<<" "<<ans.second<<endl;
        i++;
    }

    return 0;
}

pair<int,int> solve(string &v, int R, int C, int rPos, int cPos){

    vector<vector<int>> m(R, vector<int> (C,0));
    pair<int,int> ans;

    m[rPos][cPos] = 1;

    
    //bool flag = true;
    for(auto d: v){
        int x,y;
        x = 0;
        y= 0;

        if(d == 'N'){
            x = -1;
        }
        else if(d == 'S'){
            x = 1;
        }
        else if(d == 'E'){
            y = 1;
        }
        else{
            y = -1;
        }

        while(m[rPos][cPos]!=0){
            rPos += x;
            cPos += y;
            //flag = false;
        }

        m[rPos][cPos] = 1;


    }

    ans.first = rPos+1;
    ans.second = cPos+1;

    //cout<<ans.first<<" "<<ans.second<<endl;

    return ans;
}

pair<int,int> anotherSolve(string &v, int R, int C, int rPos, int cPos){
    set<pair<int, int>> s;

    s.insert({rPos, cPos});

    for(auto d:v){
        int x,y;
        x = 0;
        y = 0;

        if(d == 'N'){
            x = -1;
        }
        else if(d == 'S'){
            x = 1;
        }
        else if(d == 'E'){
            y = 1;
        }
        else{
            y = -1;
        }


        while(s.find({rPos,cPos}) != s.end()){
            rPos += x;
            cPos += y;
        }

        s.insert({rPos,cPos});
    }

    return {rPos+1,cPos+1};

}