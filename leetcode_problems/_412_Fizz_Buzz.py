from typing import List

class Solution:
    def fizzBuzzString(self, i: int):
        return 'Fizz' if i % 3 == 0 else '' + 'Buzz' if i % 5 == 0 else '' + '' if i % 3 == 0 or i % 5 == 0 else str(i)

    def fizzBuzz(self, n: int) -> List[str]:
        return [self.fizzBuzzString(i) for i in range(1, n + 1)]
