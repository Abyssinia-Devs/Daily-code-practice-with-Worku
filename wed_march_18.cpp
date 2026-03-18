#include<vector>
using namespace std;
class Solution {
public:
    char nextGreatestLetter(const vector<char>& letters, char target) {
        for (char i: letters)
        {
            if (target<i)
            {
                return i;
            }
            
        }
        return letters[0];
    }
};

int main()
{
    Solution s1;
    s1.nextGreatestLetter({'a', 'b', 'c'}, 'd');

}