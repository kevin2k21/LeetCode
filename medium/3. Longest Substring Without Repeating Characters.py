class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = []
        m = 0
        count = 0
        for i in s:
            if i not in win:
                win.append(i)
                count += 1
            else:
                m = max(m,count)
                for j in range(len(win)):
                    ini = win.pop(0)
                    count -= 1
                    if ini == i:
                        win.append(i)
                        count += 1
                        break
        return max(m,count)



sol = Solution()
print(sol.lengthOfLongestSubstring("yfsrsrpzuya"))
