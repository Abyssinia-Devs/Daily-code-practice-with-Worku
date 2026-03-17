#include <string>
#include <algorithm>
#include <format>
class Solution {
public:
    int binaryGap(int n) {
        std::string binary = std::format("{:b}", n); //1001110
        int start = 0;
        int end = 0;
        int result = 0;
        int l = binary.length();
        for (int i=0; i<l; ++i )
        {
            
            if (start < i && binary[i]=='1')
            {
                end = i - start;
                result = std::max(end, result);
            }
            if (binary[i] == '1')
                start = i;
        }
        return result;
    }

};
// It works for all input but what if we have binary like 01? it calculate the distance =1 but it is 0
// so let's find other solution

class Solution {
public:
    int binaryGap(int n) {
        std::string binary = std::format("{:b}", n); //1001110
        int one_seen_before_at = -1; // There is no 1 initially
        int max_distance = 0;

        for (int i=0; i<binary.length(); ++i )
        {
            if (binary[i] == '1') 
            {
                if (one_seen_before_at != -1)
                {
                    max_distance = std::max(max_distance, i - one_seen_before_at);
                }
                one_seen_before_at = i;
            }
        }
        return max_distance;
    }

};
