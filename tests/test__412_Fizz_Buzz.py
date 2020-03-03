#!/usr/bin/env python3

from leetcode_problems._412_Fizz_Buzz import Solution

def test_Solution():

    sol = Solution()
    assert sol.fizzBuzz(1) == ['1']
    assert sol.fizzBuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
    assert sol.fizzBuzz(16) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
                                '11', 'Fizz', '13', '14', 'FizzBuzz', '16']
