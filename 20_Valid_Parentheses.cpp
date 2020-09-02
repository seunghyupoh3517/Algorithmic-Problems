/* https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
*/
#include <iostream>
#include <stack>
#include <unordered_map>
#include <cmath>
#include <string>
using namespace std;
bool parentheses(string s);

int main(){

    cout << boolalpha; // Format flag is set -> bool values are inserted/extracted  by their textual representation

    string s1 = "()("; // False
    cout << parentheses(s1) << endl;
    string s2 = "()[]{}"; // True
    cout << parentheses(s2) << endl;
    string s3 = "(]"; // False
    cout << parentheses(s3) << endl;
    string s4 = "([)]"; // False
    cout << parentheses(s4) << endl;
    string s5 = "{[]}"; // True
    cout << parentheses(s5) << endl;
    string s6 = "";  // True
    cout << parentheses(s6) << endl;
}

bool parentheses(string s){
    // empty string consider as valid
    if(s.length()==0)
        return true;
    
    // Set up - Stack, Map
    stack<char> opening;
    unordered_map<char, char> closing;
    closing[')'] = '(';
    closing['}'] = '{';
    closing[']'] = '[';

    // Linearly read char in input
    for(int i = 0; i < s.length(); i++){
        // If it is cloisng braket
        if(s[i] == ')' || s[i] == '}' ||s[i] == ']'){ 
            char check = opening.top();
            opening.pop(); // Some suggests I should check if the stack is empty but if its empty when we saw the closing braket, that means its false already
                           // Closing bracket must not come before opening braket

            // To check the value of key(closing braket=s[i]) matches the openning bracket which we gonna POPOPOP
            if(closing.at(s[i]) != check) // .at access the value of the (key)
                return false;
        }
        // If it is opening bracket
        else
            opening.push(s[i]);
    }
    return opening.empty();
}