"""
https://codingbat.com/prob/p126968
centered_average
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""


# fromkeys(list, value - optional) creates a new dictionary with keys from list set to key, value to value
def centered_average(nums):
    nums = list(dict.fromkeys(nums))
    min_value = min(nums)
    max_value = max(nums)
    nums.remove(min_value)
    nums.remove(max_value)
    
    for i in range(len(nums)):
      sum += nums[i]
      
    return sum / len(nums)
