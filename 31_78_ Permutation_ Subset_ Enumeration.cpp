#include <iostream>
#include <cmath>
#include <vector>
#include <list>
using namespace std;
void next_permutation(std::vector<int>& nums); // Permutation Enumeration Problem
void h_reverse(std::vector<int>& nums, int from, int to);
void next_subset(std::vector<int>& nums);// Subset Enumeration Problem - Powerset Enumeration 

// Vector is type of dynamic array which has the ability to resize automatically after insertion or deletion of elements. The elements in vector are placed in
// contiguous storage so that they can be accesed and traversed using iteratiors. Element is inserted at the end of the vector.
// List is a double linked sequence that supports both forward and backward traversal. The time taken in the insertion,  deletion in the beginning, end, and middle is 
// constant. It has the non-contiguous memory and there is no pre-allocated memory.
// Python List is rather close to C++ Vector than C++ List

/*  Run with g++ -std=c++11
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
*/   
int main(){

    std::vector<int> num1 = {1,2,3};
    std::vector<int> num2 = {3,2,1};
    std::vector<int> num3 = {1,1,5};

    cout <<"before modifying nums : ";
    for(int i = 0; i < num1.size(); i++)
        cout << num1[i] << " ";

    next_permutation(num1);
    cout << endl <<  "after modifying nums : ";
    for(int i = 0; i < num1.size(); i++)
        cout << num1[i] << " ";
    cout<<endl;


    cout <<"before modifying nums : ";
    for(int i = 0; i < num2.size(); i++)
        cout << num2[i] << " ";

    next_permutation(num2);
    cout << endl <<  "after modifying nums : ";
    for(int i = 0; i < num2.size(); i++)
        cout << num2[i] << " ";
    cout<<endl;

    cout <<"before modifying nums : ";
    for(int i = 0; i < num3.size(); i++)
        cout << num3[i] << " ";

    next_permutation(num3);
    cout << endl <<  "after modifying nums : ";
    for(int i = 0; i < num3.size(); i++)
        cout << num3[i] << " ";

    cout << endl << endl;
    std::vector<int> num4 = {1,2,3};
    cout <<"Input: nums4 = ";
    for(int i = 0; i < num4.size(); i++)
        cout << num4[i] << " ";
    next_subset(num4);
}

void next_permutation(std::vector<int>& nums){
    int n = nums.size();
    int k = 0;
    int r = 0;
    
    // First, find index k which is the rightmost index of nums[k] < nums[k+1] if can't find then nums is at the last permutation
    for(int i = 0; i < n-1; i++){
        if(nums[i] < nums[i+1])
            k = i;
    }
    if(k==0)
        h_reverse(nums, 0, n-1);
    // Was going to use break in order to remove unnecessary part of coding but break can only be used in loop or switch
    
    // Second, find index r which is the rightmost index of nums[k] < nums[r], it could be k+1. And swap nums[k] and nums[r]
    int k1 = k;
    while(k < n-1 && k!=0){
        if(nums[k] < nums[k+1])
            r = k+1;
        k++;
    }

    if(k1!=0){
        swap(nums[k1], nums[r]);    
        // Third, reverse from index k+1 to end
        h_reverse(nums, k1+1, n-1);
    } 
}

void h_reverse(std::vector<int>& nums, int from, int to){
    while(from < to){
        int temp = nums[from];
        nums[from] = nums[to];
        nums[to] = temp;
        from++;
        to--;
    }
}

 /* 78.Subsets
        :type nums: List[int]
        :rtype: List[List[int]]
*/
void next_subset(std::vector<int>& nums){
    // Use bit-wise operation - subset problem is basically whether each element is included or not, 1 or 0
    int n = nums.size();
    int p_n = pow(2, n); 
    // Outerloop : each possible bitstring
    for(int counter = 0; counter < p_n; counter++){
        cout << endl << "[ ";
        // innerloop: print members of given set by checking the memberhsip
        for(int i = 0; i < n; i++){
            if(counter & (1<<i))
                cout << nums[i] << " ";
        }
        cout << "]";
    }
}




/* David's Solution using python - which basically have similar logic with me

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def inplaceReverse(array, start, end):
            # swapping start & end until it is no longer start < end
            while start < end:
                array[start], array[end] = array[end], array[start]
                start+=1
                end-=1
            return array
        
        # Algorithm
        # 1. find the last k s.t. nums[k]<nums[k+1]
        # 1.a if there is no nums[k] < nums[k+1], reverse the entire nums
        inflection_point = -1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                inflection_point = i
        if inflection_point==-1:
            return inplaceReverse(nums, 0, len(nums)-1)
        # 2. find the largest k s.t. nums[k] > nums[inflection_point]
        swap_index = -1
        for i in range(len(nums)):
            if nums[i] > nums[inflection_point]:
                swap_index=i
        # 3. swap
        nums[swap_index], nums[inflection_point] = nums[inflection_point], nums[swap_index]
        # 4. reverse inflection_point thereafter.
        return inplaceReverse(nums, inflection_point+1, len(nums)-1) 
*/
