// CPP program To calculate The Value Of nCr
#include <bits/stdc++.h>
using namespace std;


// Returns factorial of n
long fact(int n)
{
      if(n==0)
      return 1;
    long res = 1;
    for (int i = 2; i <= n; i++)
        res = res * i;
    return res;
}

long nCr(int n, int r)
{
    return fact(n) / (fact(r) * fact(n - r));
}



// Driver code
int main()
{
    long count = 0;
    long n;
    cin >> n;
    for(long i=1; i<(n+1); i++){
        cout << nCr(i*i,2) - count << endl;
        count += 8 * (i-1);
    }
    return 0;
}