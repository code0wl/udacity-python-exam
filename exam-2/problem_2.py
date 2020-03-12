import os


def find_files(suffix, path):
    if path[-2:] == suffix:
        print("path matched: ", path)
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                find_files(suffix, os.path.join(path, file))


# Test cases

# match
find_files(".h", "exam-2/testdir")
# no match
find_files(".o", "exam-2/testdir")

# output:
# exam-2/testdir/subdir3/subsubdir1/b.h
# exam-2/testdir/subdir5/a.h
# exam-2/testdir/t1.h
# exam-2/testdir/subdir1/a.h
