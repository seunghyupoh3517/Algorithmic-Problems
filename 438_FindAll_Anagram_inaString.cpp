/* https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
*/
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
std::vector<int> findAnagrams(string s, string p);
bool compare_count(char x[], char y[]);

int main(){
    std::vector<int> result;
    string s1 = "cbaebabacd";
    string p1 = "abc";
    result = findAnagrams(s1, p1);
    for(int i = 0; i < result.size(); i++)
        cout << result[i] << " ";

    cout << endl;
    string s2 = "abab";
    string p2 = "ab";
    result = findAnagrams(s2, p2);
     for(int i = 0; i < result.size(); i++)
        cout << result[i] << " ";
}

std::vector<int>findAnagrams(string s, string p){
    std::vector<int> result;
    int n = s.size();
    int target = p.size();

    // size of ASCII Code 256 - to make sure we can cover all the characters
    char count_s[256] = {0};
    char count_p[256] = {0};

    // count s of window size p and p 
    for(int i = 0; i < target; i++){
        (count_s[s[i]])++;
        (count_p[p[i]])++;
    }

    // ------- 
    // -- 
    // Current
    //  --
    //   --
    //    --
    //     --
    //      --
    for(int i = target; i < n; i++){
        if(compare_count(count_s, count_p)) // if two count arrays correspond
            result.push_back(i - target); // add element
        
        // slide to next window size
        // add next char, remove the first character
        count_s[s[i]]++;
        count_s[s[i-target]]--;
    }
    // Need to compare n - target + 1 times, so the last comparison
    if(compare_count(count_s, count_p)) // if two count arrays correspond
            result.push_back(n - target); // add element

    return result;
}

bool compare_count(char x[], char y[]){
    for(int i = 0; i < 256; i++){
        if(x[i] != y[i])
            return false;
    }
    return true;
}