'''
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:  Input: bits = [1, 0, 0]         Output: True
Explanation:
The only way to decode it is two-bit character(10) and one-bit character(0). So the last character is one-bit character.

Example 2:      Input: bits = [1, 1, 1, 0]      Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

ANS =>
We don't need to traverse the whole array, just check the last part of it.

if there is only one symbol in array the answer is always true (as last element is 0)
if there are two 0s at the end again the answer is true no matter what the rest symbols are( ...1100, ...1000,)
if there is 1 right before the last element(...10), the outcome depends on the count of sequential 1, i.e.
a) if there is odd amount of 1(10, ...01110, etc) the answer is false as there is a single 1 without pair
b) if it's even (110, ...011110, etc) the answer is true, as 0 at the end doesn't have anything to pair with
'''

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits

        if bits == [0] or bits[(len(bits)-2):] == [0, 0]:
            return True
        elif bits[0] == 0:
            bits.pop(0)
        if len(bits) == 2:
            return False

        while len(bits) > 1:
            remain = bits.pop(0)
            if remain == 1:
                bits.pop(0)
            if bits == [0] and len(bits) == 1:
                return True
        return False




cl = Solution()
print('T: ', cl.isOneBitCharacter([0]))            #T
print('T: ', cl.isOneBitCharacter([1, 0, 0]))      #T
print('F: ', cl.isOneBitCharacter([1, 0]))         #F
print('F: ', cl.isOneBitCharacter([0, 1, 0]))      #F

print('F: ', cl.isOneBitCharacter([1, 1, 1, 0]))   #F
print('F: ', cl.isOneBitCharacter([1, 0, 1, 0]))   #F
print('T: ', cl.isOneBitCharacter([1, 1, 0, 0]))   #T
print('T: ', cl.isOneBitCharacter([1, 1, 0]))      #T
print('T: ', cl.isOneBitCharacter([0, 1, 1, 0]))   #T
print('F: ', cl.isOneBitCharacter([1, 1, 0, 1, 0])) #F


#   option 2

''''
        if bits == [0] or bits[(len(bits)-2):] == [0, 0]:
            return True

        while len(bits) > 1:
            remain = bits.pop(0)
            if remain == 1:
                bits.pop(0)
            if bits == [0] and len(bits) == 1:
                return True
        return False
'''



