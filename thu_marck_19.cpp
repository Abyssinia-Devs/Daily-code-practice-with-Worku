#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
            std::sort(arr.begin(), arr.end());
    
    int minDiff = std::numeric_limits<int>::max();
    std::vector<std::vector<int>> result;

    // Find the minimum absolute difference
    for (size_t i = 1; i < arr.size(); ++i) {
        int diff = arr[i] - arr[i - 1];
        if (diff < minDiff) {
            minDiff = diff;
            result.clear(); // Clear previous results
            result.push_back({arr[i - 1], arr[i]}); // Add new pair
        } else if (diff == minDiff) {
            result.push_back({arr[i - 1], arr[i]}); // Add pair with the same minDiff
        }
    }

    return result;
    }
};