class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if not s:
            return 0
        mul_, s = (1, s[1:]) if s[0] == "+" else (-1, s[1:]) if s[0] == "-" else (1, s)
        idx_ = 1
        output_int = 0
        while idx_ <= len(s):
            try:
                output_int = int(s[:idx_])
            except ValueError:
                break
            idx_ += 1
        output_int *= mul_
        if output_int < -2**31:
            return -2**31
        elif output_int > 2**31 - 1:
            return 2**31 - 1
        else:
            return output_int


if __name__ == '__main__':
    solution = Solution()
    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("-91283472332") == -2147483648
    assert solution.myAtoi("") == 0
    assert solution.myAtoi("      -11919730356x") == -2147483648


