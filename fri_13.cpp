
#include<algorithm>
#include <string>
#include<iostream>
using namespace std;
class Solution {

public:

    int minOperations(string s) {

        int n = s.length();

        int start_0 = 0; //01010101...
        int start_1 = 0; //10101010



        for (int i = 0; i < n; i++) {

            // Check against the two patterns
            bool is_even = i%2==0; // at index 0,2,4 
            if (is_even) { // at even index for start_0 there will be 0

                if (s[i] == '1') start_0++; // there is a difference

                if (s[i] == '0') start_1++; 

            } else { // if odd

                if (s[i] == '0') start_0++; 

                if (s[i] == '1') start_1++;

            }

        }

        return min(start_0, start_1);

    }

};


int main() {
    Solution sol;
    std::string s = "101010110000010001";
    int result = sol.minOperations(s);
    std::cout<<result;
    return 0;
}