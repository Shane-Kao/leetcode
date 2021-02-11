import math


class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        pow_ = 0
        x_ = abs(x)
        while x_:
            log_ = math.log10(x_)
            float_part = log_ - int(log_)
            first_digit = int(10**float_part)
            output += first_digit * 10**pow_
            int_part = int(log_)
            x_ -= first_digit * 10**int_part
            if not x_:
                break
            pow_ += int_part - int(math.log10(x_))
        output = output if x >= 0 else -output
        if output > 2**31 - 1 or output < -2**31:
            return 0
        return output


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(1234512) == 2154321
    assert solution.reverse(120) == 21
    assert solution.reverse(123) == 321
    assert solution.reverse(0) == 0
    assert solution.reverse(-123) == -321
    assert solution.reverse(901000) == 109
    assert solution.reverse(1534236469) == 0