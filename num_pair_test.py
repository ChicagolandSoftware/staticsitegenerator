#!/usr/bin/env python3
'''
for a list of numbers, and a number k, find all numbers in the list that add up to k
only for pairs
example:
nums = [1, 5, 24, 9, 2, 3, 8]
k = 10
'''
# read about a python interview question so I decided to make my own solution for it

# function to find out if a pair in a list called nums adds up to a number k
def sum_pair(nums, k):
    pairs_found = 0  # increment upon finding a pair that adds up to k
    for num in nums: # iterate through the list
        nums.remove(num) # if you don't remove it, then it will say (5, 5) is a pair, but it only occurs once
        complement = k - num # complement is what you're looking for
        # print("testing: num - k = " + str(complement)) # I did this to test when I was building the solution
        for item in nums: # look through list again and compare the difference to the items in the list
            if item == complement:
                print("pair found: " + str(item) + ", " + str(num))
                pairs_found += 1
    if pairs_found == 0:
        print("no pairs found!")
    return pairs_found != 0  # true = pairs were found, false = pairs were not found
# example list and k values


print("list 1 and k 1:")
sum_pair([1, 5, 24, 9, 2, 3, 8], 10)
print("list 2 and k 2:")
sum_pair([4, 5, 24, 11, 2, 7, 8, 3, 10, 6, 0], 11)
print("list 3 and k 3:")
sum_pair([0, 7, 12, 29, 42], 150)
