from typing import List

class Solution:
    def fizzBuzzString(self, i: int):
        return 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) + str(i) * (i % 3 != 0 and i % 5 != 0)

    def fizzBuzz(self, n: int) -> List[str]:
        return [self.fizzBuzzString(i) for i in range(1, n + 1)]
