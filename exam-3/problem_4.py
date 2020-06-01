def sort_012(input_list):

    if not isinstance(input_list, list) or not len(input_list):
        return []

    last_list_item = len(input_list) - 1

    halfway, start = 0, 0
    end = last_list_item - start

    while end >= halfway:
        print('what am I?', halfway, end)
        if not input_list[halfway]:
            input_list[start], input_list[halfway] = input_list[halfway], input_list[start]
            halfway += 1
            start += 1
        elif input_list[halfway] == 1:
            halfway += 1
        else:
            input_list[halfway], input_list[end] = input_list[end], input_list[halfway]
            end -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Tests

print("Test 1 - Normal")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print("Test 2 - Edge")
test_function([0])
test_function([])
test_function('')
