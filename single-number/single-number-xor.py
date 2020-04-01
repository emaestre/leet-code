import sys


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        current = 0
        for num in nums:
            current ^= num

        return current


def stringToIntegerList(input):
    return json.loads(input)


def main():
  import io

   def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)

            ret = Solution().singleNumber(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break
