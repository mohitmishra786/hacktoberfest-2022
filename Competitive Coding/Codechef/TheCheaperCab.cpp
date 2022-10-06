#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    int t = 1;
    cin >> t;
    while (t--)
    {
        int x, y;
        cin >> x >> y;
        if (x > y)
            cout << "\nSecond";
        else if (x == y)
            cout << "\nAny";
        else

            cout << "\nFirst";
    }
    return 0;
}
