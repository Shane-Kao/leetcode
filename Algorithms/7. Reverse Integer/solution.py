class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        x_ = -x if x < 0 else x
        while x_:
            output = output * 10 + x_ % 10
            x_ = int(x_ / 10)
        if output > 2**31 - 1 or output < -2**31:
            return 0
        return -output if x < 0 else output


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(1234512) == 2154321
    assert solution.reverse(120) == 21
    assert solution.reverse(123) == 321
    assert solution.reverse(0) == 0
    assert solution.reverse(-123) == -321
    assert solution.reverse(901000) == 109
    assert solution.reverse(1534236469) == 0