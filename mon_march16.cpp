#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n =0;
        for(auto x: nums)
        {
           n ^=x;
        }
        return n;
    }
};