# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# nums = [2,7,11,15]
# def add_two(nums,target):
# #     n = len(arr)
# #     for i in range(n-1):
# #         for j in range(i-1,n):
# #             if arr[i]+arr[j] == target:
# #                 return [i,j]
# #             # print('this is j',arr[j])
# #         print(arr[i])
# #     return []
#     numList = {}
#     for i,n in enumerate(nums):
#         diff = target - n
#         print('this is the difference',diff)
#         if diff in numList:
#             return [numList[diff],i]
#         else:
#             numList[n] = i



# print(add_two(nums,22))
# nums_list = {}
# target = 9
# for i,n in enumerate(nums):
#     print(i,n)
#     diff = target-n
#     print('this is the differnce',diff)
#     if diff in nums_list:
#         print('answer',[nums_list[diff],i])
#     else:
#         print([nums_list[n],i])



nums = [2,7,11,15]
n = len(nums)  # length = 4
target = 9
for i in range(n-1):
    print('this is i',nums[i])
    for j in range(i+1,n):
        print('this is the j',nums[j])
        if nums[i]+nums[j] == target:
            print('this is the result',[i,j])

