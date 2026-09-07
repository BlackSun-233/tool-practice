def count_even(num_list):
    """统计列表中偶数的个数"""
    count = 0
    for num in num_list:
        if num % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    test_data = [1, 2, 3, 4, 5, 6, 7, 8]
    print(count_even(test_data))
