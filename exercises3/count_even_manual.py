def count_even(num_list):
    cnt = 0
    for i in num_list:
        if i % 2 == 0:
            cnt = cnt + 1
    return cnt


test = [1,2,3,4,5,6,7,8]
print(count_even(test))
