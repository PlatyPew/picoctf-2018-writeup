#!/usr/bin/python
# Author: plusline (https://github.com/plusline)
# Modified by: PlatyPew

from pwn import *


def solve(problem):
    problem = problem.split(' + ')

    num = []

    for one in problem:
        count = 0
        max_c = 0

        for i in range(len(one)):
            if one[i] == '(':
                count += 1
            elif one[i] == ')':
                count -= 1
            max_c = max(max_c, count)
        num = num + [max_c]

    def combine(str1, str2, num1, num2):
        if num1 < num2:
            return '(' + str1 + str2[1:]
        elif num1 > num2:
            return str1[0:-1] + str2 + ')'
        elif num1 == num2:
            return str1+str2

    ans = problem[0]
    num_total = num[0]
    for i in range(1, len(problem), 1):
        ans = combine(ans, problem[i], num_total, num[i])
        num_total = max(num_total, num[i])

    return ans

def main():
    s = remote('2018shell.picoctf.com', 7866)
    for i in range(14):
        s.recvline()

    problem = s.recvline().strip()
    ans = solve(problem.split('=')[0].strip())
    print(ans)


if __name__ == '__main__':
    main()
