// Author: πα

#include <bits/stdc++.h>
using namespace std;
#define long int64_t

int main()
{
    int n, k;
    cin >> n >> k;
    n += n;
    vector<int> v(n);
    for (int& it : v)
        cin >> it;
    sort(v.begin(), v.end());
    int ans = INT_MAX;
    do {
        int cost = 0, cap = 0;
        for (int i = 0; i < n; i += 2) {
            if (v[i] > v[i + 1])
                ++cost;
            cap += v[i];
        }
        if (cap >= k)
            ans = min(ans, cost);
    } while (next_permutation(v.begin(), v.end()));
    cout << (ans == INT_MAX ? -1 : ans) << '\n';
    return 0;
}
