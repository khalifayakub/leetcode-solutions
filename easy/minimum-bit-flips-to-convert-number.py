class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start^goal).count('1')


# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         start_bits = bin(start).split('0b')[1]
#         goal_bits = bin(goal).split('0b')[1]
#         n = len(start_bits)
#         m = len(goal_bits)
#         if m > n:
#             bits = ['0'] * (m-n)
#             start_bits = str(''.join(bits)) + start_bits
#         else:
#             bits = ['0'] * (n-m)
#             goal_bits = str(''.join(bits)) + goal_bits
#         count = 0
#         for i in range(len(start_bits)):
#             if start_bits[i] != goal_bits[i]:
#                 count += 1
#         return count