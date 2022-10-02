#include <bits/stdc++.h>
using namespace std;

vector<int> merge (vector<int> a, vector<int> b) {
    int m = a.size();
    int n = b.size();

    vector<int> c;
    int p1 = 0;
    int p2 = 0;
    while(p1<m && p2<n) {
        if (a[p1]<=b[p2]) {
            c.push_back(a[p1]);
            p1++;
        } else {
            c.push_back(b[p2]);
            p2++;
        }
    }
    if (p1<m) {
        while(p1<m) {
            c.push_back(a[p1]);
            p1++;
        }
    }

    if (p2<n) {
        while(p2<n) {
        c.push_back(b[p2]);
        p2++;
        }
    }
    return c;
}

void print (vector<int> c) {
    for (int i: c) {
        cout << i << " ";
    }
}

int main() {
    vector<int> a = {2, 3, 5, 7, 9};
    vector<int> b = {1, 2, 4, 6, 8};
    vector<int> c;
    c = merge(a, b);
    print(c);

    return 0;
}
