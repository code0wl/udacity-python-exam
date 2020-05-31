not_found = -1


def rotated_array_search(input_list, target):

    if len(input_list) == 0:
        return not_found

    pivot = pivot_search(input_list, 0, len(input_list) - 1)

    if pivot == not_found:
        return search(input_list, target, 0, len(input_list - 1))

    pivot_value = input_list[pivot]

    if target == pivot_value:
        return pivot

    if target < pivot_value and target >= input_list[0]:
        return search(input_list, target, 0, pivot)

    return search(input_list, target, pivot + 1, len(input_list) - 1)


def linear_search(input_list, number):
    if len(input_list) == 0:
        return not_found

    for index, element in enumerate(input_list):
        if element == number:
            return index


def pivot_search(input_list, left, right):
    if left > right:
        return not_found
    if left == right:
        return left
    halfway = (left + right) // 2
    current_halfway = input_list[halfway]

    if halfway < right and current_halfway > input_list[halfway + 1]:
        return halfway
    if halfway > left and current_halfway < input_list[halfway - 1]:
        return pivot_search(input_list, left, halfway - 1)

    return pivot_search(input_list, halfway + 1, right)


def search(input_list, target, left, right):
    if left > right:
        return not_found

    halfway = (left + right) // 2
    current_halfway = input_list[halfway]

    if current_halfway == target:
        return halfway
    if target < current_halfway:
        return search(input_list, target, left, halfway - 1)

    return search(input_list, target, halfway + 1, right)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


print("Test 1 - Normal")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # -1

print("Test 2 - Edge")
test_function([[6], 6])  # only one item 0
test_function([[], -1])  # only one item -1
