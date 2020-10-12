#include <bits/stdc++.h>
#define endl "\n"
#define fastio               \
    ios::sync_with_stdio(0); \
    cin.tie(0);              \
    cout.tie(0);
using namespace std;
#define ll long long int

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll n, x, p, k;
        cin >> n >> x >> p >> k;
        ll a[n];
        for (ll i = 0; i < n; i++)
            cin >> a[i];

        sort(a, a + n);
        p = p - 1;
        k = k - 1;

        int op = -1;
        if (a[p] == x)
            op = 0;
        else if (k > p && a[p] < x || k < p && a[p] > x)
        {
            op = -1;
        }
        else if (k >= p && a[p] > x)
        {
            op = 0;
            for (ll i = p; i >= 0 && a[i] > x; i--)
            {
                op++;
                if (i == 0)
                    break;
            }
        }
        else if (k <= p && a[p] < x)
        {
            op = 0;
            for (long long int i = p; i < n && a[i] < x; i++)
            {
                op++;
                if (i == (n - 1))
                    break;
            }
        }

        cout << op << endl;
    }
    return 0;
}