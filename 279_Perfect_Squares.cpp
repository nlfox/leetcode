#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    int numSquares(int n) {
        unsigned int inf = INT32_MAX;
        int *dp = new int[n + 1];
        for (int j = 1; j <= n; ++j) {
            dp[j] = j;
        }
        for (int i = 1; i <= ceil(sqrt(n)); ++i) {
            dp[i * i] = 1;
        }
        for (int k = 1; k <= n; ++k) {
            for (int i = (int) sqrt(k); i * i * dp[k] > k; --i) {
                dp[k] = min(dp[k], 1 + dp[k - i*i]);
            }
        }
        return dp[n];
    }
};

int main() {
    cout << "res " << Solution().numSquares(9975) << endl;
    return 0;
}