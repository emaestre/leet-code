if __name__ == '__main__':
    main()

    class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        
        for num in nums:
            if(num in count_map):
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        for key in count_map:
            if(count_map[key] == 1):
                return key

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().singleNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()