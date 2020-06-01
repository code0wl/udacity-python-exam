def rearrange_digits(input_list):

    if not input_list or len(input_list) == 1 or not isinstance(input_list, list):
        return []

    input_list = merge_and_sort(input_list)

    is_even = len(input_list) % 2 == 0

    start_num, end_num = '', ''

    start = True

    for i in range(len(input_list) - 1, -1, -1):
        is_last = i == len(input_list) - 1
        if start:
            start_num += str(input_list[i])
        else:
            end_num += str(input_list[i])
        if is_last and not is_even:
            continue

        if start:
            start = False
        else:
            start = True

    return int(start_num), int(end_num)


def merge(start_arr, end_arr):
    arr = []
    i, j = 0, 0
    while i < len(start_arr) and j < len(end_arr):
        if start_arr[i] < end_arr[j]:
            arr.append(start_arr[i])
            i += 1
        else:
            arr.append(end_arr[j])
            j += 1

    arr = arr + start_arr[i:]
    arr = arr + end_arr[j:]

    return arr


def merge_and_sort(arr):

    if len(arr) == 1:
        return arr

    midway = len(arr) // 2
    start = arr[:midway]
    end = arr[midway:]

    start = merge_and_sort(start)
    end = merge_and_sort(end)

    return merge(start, end)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Tests


print("Test 1 - Normal")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1, 1, 1], [22]])
test_function([[8, 0, 1, 5, 0], [850, 10]])

print("Test 2 - Edge")
test_function([[1], []])
test_function([[], []])
test_function(['hello world', []])
