# Given an array of integers, find two numbers in it such that they can add up to a specific number.
# You may assume there are exactly one solution, you can’t use the same element twice.
# (Only time-complexity optimized solution gets full grade)

# Example:
# Given [2, 7, 11, 4], Target = 13.
# The answer is 2 and 11.

# Modify the “solution” function in the question1.py.
# (Analyze your time complexity)


def solution(list_num, num):
    a = 0
    b = 0
    # '''type in your solution, find a and b in array that a+b=num'''
    # list needs to be organized
    list_dic = {}
    for i, x in enumerate(list_num):
        # num = a + b
        diff = num - x
        if diff in list_dic:
            a = x
            b = diff

        list_dic[list_num[i]] = i
    if a ==0 and b ==0:
        return 'No solution with given list. Output was (0,0)'
    return a, b


numbers = [0, 21, 78, 19, 90, 13]
print(solution(numbers, 21))
print(solution(numbers, 25))

# Looking at how data is processed, the number is checked element by element for the matching pair.
# In the worst case, the components are found by looping through the entire list.
# So it would be [(n-1) + (n-2) + (n-#)] and so on. The simplified version leads to [n(n-1)]/2, which is n^2 simplified.
# Time complexity in worst case is O(n^2)
# But if running though the list once (cannot use the same element twice)
# Time complexity would be O(n)

# numb = [2, 7, 11, 4]
# print(solution(numb, 13))
# The answer is 2 and 11.
