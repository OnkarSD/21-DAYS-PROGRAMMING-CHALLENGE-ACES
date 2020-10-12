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
   ll tc;
   cin >> tc;
   while (tc--)
   {
       ll n, k,v;
       ll days = 0;
       cin >> n >> k;
       ll r[n];
       for (int i = 0; i < n; i++)
           cin >> r[i];
       ll i = 0;
       while (i < n)
       {
           v = r[i];
           if (v >= k)
           {
               days = days +1;
               r[i + 1] += (v - k);
           }
           if (v < k)
               break;
            i++;
       }
       ll x = ((r[n - 1] - k) / k);
       if (i == n)
       {
           days = days + x ;
       }
       cout << days+1 << endl;
   }
}
