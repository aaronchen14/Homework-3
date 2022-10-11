# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Modify the “solution” function in the question5.py. (Analyze your time complexity)


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        sym_dic = {'(' : ')',
                   '{' : '}',
                   '[' : ']'}
        # for i, x in enumerate(list_num):
        # num = a + b
        holder = []
        for x in s:
            if x in sym_dic.keys():
                holder.append(x)
            else:
                y = holder.pop()
                if x != sym_dic[y]:
                    return False
        return True


q5_input = '{([[]()])}'
outcome = Solution().isValid(q5_input)
print(outcome)

# The string is only being ran through once, so time complexity would be O(n)
