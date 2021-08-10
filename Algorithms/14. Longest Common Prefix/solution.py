class Solution:
    def longestCommonPrefix(self, strs):
        pre = strs[0]
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        return pre