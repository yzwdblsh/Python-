def counts(string, substring):
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    for i in range(str_len - sub_len + 1):
        if string[i:i + sub_len] == substring:
            count += 1
    return count


main_string = "hello world hello hello"
sub_string = "ld"
print("子串出现的次数:", counts(main_string, sub_string))
