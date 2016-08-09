# coding=utf-8

"""
    question url: https://leetcode.com/problems/zigzag-conversion/
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = []
        for i in range(numRows):
            base = i
            if i == 0 or i == numRows-1:
                while base < len(s):
                    zigzag.append(s[base])
                    base = base + 2 * numRows - 2
            else:
                step = 2 * numRows-2-2*i
                while True:
                    if base < len(s):
                        zigzag.append(s[base])
                    else:
                        break
                    if base + step < len(s):
                        zigzag.append(s[base+step])
                        base = base + 2 * numRows - 2
                    else:
                        break
        return ''.join(zigzag)