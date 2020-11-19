"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
Example 1:
Input: n = 5            Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3            Output: [-1,0,1]

Example 3:
Input: n = 1            Output: [0]

Constraints:
1 <= n <= 1000
"""

from typing import List

class Solution2:
    def sumZero(self, n: int) -> List[int]:
        n = n
        print(sum(list(range(1-n,n,2))))
        return list(range(1-n, n, 2))

        #return list(range(1, n)) + [-(n-1)*(n)//2]

cl = Solution2()
print()
print(cl.sumZero(1000))
print(cl.sumZero(3))
print(cl.sumZero(6))


#********************************************************************
#********************************************************************


class Solution1:
    def sumZero1(self, n: int) -> List[int]:
        res = []
        if (n % 2 == 0):
            for i in range(1, n+1, 2):
                res.append(i)
                res.append(i * -1)
                print(i)
        else:
            res.append(0)
            for i in range(1, n-1, 2):
                res.append(i * -1)
                res.append(i)
        return res


cl = Solution1()
print()
print(cl.sumZero1(5))
print(cl.sumZero1(3))
print(cl.sumZero1(6))
