import random


def get_min_max(ints):
    if len(ints) >= 1:
        min = ints[0]
        max = ints[0]
        for num in ints:
            if num < min:
                min = num
            if num > max:
                max = num

        return (min, max)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Test 1 - Normal")
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((0, 120) == get_min_max(
    [100, 6, 52, 0, 120, 0])) else "Fail")  # (0, 120)
print("Pass" if ((5, 800) == get_min_max(
    [5, 6, 12, 800])) else "Fail")  # (5, 800)
print("Pass" if ((1, 300) == get_min_max(
    [1, 2, 3, 4, 5, 100, 20, 300, 40, 102, 102])) else "Fail")  # (1, 300)

print("Test 2 - Edge")
print("Pass" if ((1, 1) == get_min_max([1])) else "Fail")  # (1, 1)
print("Pass" if ((.19, 1) == get_min_max([1, .19])) else "Fail")  # (.19, 1)
print("Pass" if ((100, 100) == get_min_max(
    [100, 100])) else "Fail")  # (100, 100)
