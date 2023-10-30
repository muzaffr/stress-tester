// Author: πα

#include <bits/stdc++.h>
using namespace std;
#define long int64_t

void solve()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    int o = 0;
    for (int i = 0; i < n; ++i)
        o += s[i] == '1';
    if (2 * o != n) {
        cout << "-1\n";
        return;
    }
    vector<int> ans;
    for (int i = 0, j = n; i < j; ++i) {
        n = (int) s.length();
        j = n - i;
        if (s[i] == s[j - 1]) {
            if (s[i] == '0') {
                s.insert(s.begin() + j, '1');
                s.insert(s.begin() + j, '0');
                ans.push_back(j);
            } else {
                s.insert(s.begin() + i, '1');
                s.insert(s.begin() + i, '0');
                ans.push_back(i);
            }
        }
    }
    cout << ans.size() << '\n';
    for (int it : ans)
        cout << it << ' ';
    cout << '\n';
}

int main()
{
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
