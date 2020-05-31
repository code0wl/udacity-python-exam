def sqrt(number):

    if number <= 1:
        return number

    high, low = 0, number

    while high <= low:
        halfway = (low + high) // 2
        found = halfway ** 2 == number or halfway ** 2 <= number < (
            halfway + 1) ** 2
        if found:
            return halfway
        elif halfway ** 2 > number:
            low = halfway
        else:
            high = halfway

# Tests


print("Test 1 - Normal")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (8 == sqrt(64)) else "Fail")

print("Test 2 - edge cases since function only handles integers")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (.9 == sqrt(.9)) else "Fail")
print("Pass" if (0.1 == sqrt(0.1)) else "Fail")
