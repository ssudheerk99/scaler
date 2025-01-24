def get_second_max(arr):
    max_ = -1
    sec_max_ = -1
    for i in arr:
        if i > max_:
            sec_max_ = max_
            max_ = i
        else:
            sec_max_ = max(sec_max_,i)
    return sec_max_


a = [4,27,44,12,56]

sec_max = get_second_max(a)
print(sec_max)