import os


def find_files(suffix, path):
    if path[-2:] == suffix:
        print("path matched: ", path)
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                find_files(suffix, os.path.join(path, file))


# Specs

# match
find_files(".h", "exam-2/testdir")
find_files(".c", "exam-2/testdir")
# no match
find_files(".o", "exam-2/testdir")
