def solution_longestSubString(s):
        #Let's use this variable for length tracking
        max_length = 1
        #Just a small edge case handling
        if s == '':
            return 0

        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in substring:
                    substring = substring + s[j]
                    max_length = max(max_length, len(substring))
                else:
                    break

        return max_length