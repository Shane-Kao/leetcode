# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
import numpy as np

class Solution:
    def _get_batch_size(self, numRows):
        return 2 * numRows - 2

    def _batch(self, iterable_, n):
        l = len(iterable_)
        for ndx in range(0, l, n):
            yield iterable_[ndx:min(ndx + n, l)]

    def _get_sub_matrix(self, s, numRows):
        X = np.array([[None] * (numRows - 1) for _ in range(numRows)])
        for idx, _ in enumerate(range(numRows - 1)):
            if idx == 0:
                if len(s) > numRows:
                    X[:, 0] = list(s[:numRows])
                else:
                    X[0:len(s), 0] = list(s)
            else:
                try:
                    X[numRows - idx - 1, idx] = s[numRows + idx - 1]
                except IndexError:
                    pass
        return X

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            s_ = ''
            batch_size = self._get_batch_size(numRows=numRows)
            X = None
            for i, j in enumerate(self._batch(s, n=batch_size)):
                X_ = self._get_sub_matrix(j, numRows)
                X = np.column_stack((X, X_)) if X is not None else X_

            for idx in range(X.shape[0]):
                s_ += ''.join([i for i in X[idx] if i is not None])
            return s_


if __name__ == '__main__':
    f = Solution().convert
    assert (f('A', 1) == 'A')
    assert (f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    assert (f("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")




