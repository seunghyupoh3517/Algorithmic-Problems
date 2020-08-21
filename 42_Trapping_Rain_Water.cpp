#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
// Run with g++ -std=c++11
int findTrap(std::vector<int> input);

int main(){
    std::vector<int> input = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << findTrap(input) << endl;
}

int findTrap(std::vector<int> input){
    int trap = 0;
    int n = input.size();
    int l = 0, M_l = 0, M_r = 0;
    int r = n-1;
    
    while (l < r){
        //cout << "l = " << l << " r = " << r << " input[l] = " << input[l] << " input[r] = " << input[r] << endl; 
        if(input[l] <= input[r]){
            M_l = max(M_l, input[l]);
            trap += M_l - input[l];
            l++;
        }
        else{
            M_r = max(M_r,  input[r]);
            trap += M_r - input[r];
            r--;
        }
        //cout << "trap = " << trap << endl;
    }

    cout << endl;
    cout << "trapped water = ";
    return trap;
}