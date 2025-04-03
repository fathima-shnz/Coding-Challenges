class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        first = strs[0]
        last = strs[-1]

        common_prefix = ""

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix += first[i]
            else:
                break

        return common_prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow", "flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))