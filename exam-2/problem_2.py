import os


def find_files(suffix, path):
    if not suffix or not path:
        return

    if path[-2:] == suffix:
        print("path matched: ", path)
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                find_files(suffix, os.path.join(path, file))


# Specs

print("Test 1 - Normal")
find_files(".h", "exam-2/testdir")
find_files(".c", "exam-2/testdir")
find_files(".o", "exam-2/testdir")

print("Test 2 - Edge different datatypes")
find_files(0, "exam-2/testdir")  # no entries
find_files(True, "exam-2/testdir")  # no entries

print("Test 3 - Edge No Entry")
find_files("", "")
