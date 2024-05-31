def lengthOfLongestSubstring(s):
    if not s:
        return 0

    res = []
    max_length = 0
    for i in s:
        if i in res:
            index = res.index(i)
            res = res[index + 1:]

        res.append(i)
        max_length = max(len(res), max_length)
    return max_length


s = "abcdfgeabcd"
print(lengthOfLongestSubstring(s))

