class Solution:
    SYMBOLS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        prev_ = 0
        result_ = 0
        for s_ in s:
            curr_ = self.SYMBOLS[s_]
            if prev_ < curr_:
                curr_ -= prev_ * 2
            result_ += curr_
            prev_ = curr_
        return result_