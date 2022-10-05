#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void file_i_o()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

void Main()
{
    /* Method 1 */
    // int n;
    // cin >> n;
    // char arr[n + 1];
    // cin >> arr;
    // bool check = true;
    // for (int i = 0; i < n; i++)
    // {
    //     if (arr[i] != arr[n - 1 - i])
    //     {
    //         check = false;
    //         break;
    //     }
    // }
    // if (check == true)
    // {
    //     cout << "Palindrome";
    // }
    // else
    // {
    //     cout << "Not Palindrome";
    // }

    /* Method 2 */
    string str;
    cin >> str;
    string temp_str = str;
    reverse(temp_str.begin(), temp_str.end());
    if (str == temp_str)
    {
        cout << "Palindrome";
    }
    else
    {
        cout << "Not Palindrome";
    }
}

int main()
{
    clock_t begin = clock();
    // file_i_o();

    Main();

#ifndef ONLINE_JUDGE
    clock_t end = clock();
    cout << "\n\nExecuted In: " << double(end - begin) / CLOCKS_PER_SEC << " seconds";
#endif

    return 0;
}

/* Input
6
racecar
*/