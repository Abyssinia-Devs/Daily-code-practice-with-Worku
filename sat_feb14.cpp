#include<algorithm>
#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    int countBinarySubstrings(std::string s) {
        /*Group consecutive equal characters and count each group’s length. Then iterate through adjacent groups, add the minimum of each pair, and return the total.*/
        std::vector<int> group_sizes {};
        int count = 1;
        for(auto i =1 ; i< s.length() ; i++) {
            if (s[i] == s[i-1]) count +=1;
            else {
                group_sizes.push_back(count);
                count =1;
            }
        }
        group_sizes.push_back(count);

        int total_count = 0;
        for (auto i=1 ; i < group_sizes.size(); i++) {
            total_count += std::min(group_sizes[i-1], group_sizes[i]);
        }
        return total_count;
    
    }
};
int main() {
    Solution s1;
    int x = s1.countBinarySubstrings("1010101010");
    std::cout<<x;
    return 0;
}