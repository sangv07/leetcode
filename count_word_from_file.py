# read total count of words from file
"""
file = open("D:\Python\Coupa_software_question.txt")
data = file.read()

words = data.split()

print("numbers: ", len(words))


#****************************************************************
#****************************************************************


# finding duplicate words and count

file = open("D:\Python\FIle_hand\python_file_read.txt", "w")
data = "My Name is Sanjiv"
file.write(data)
file.close()


#****************************************************************
#****************************************************************


# finding duplicate lines from files

with open("D:\Python\FIle_hand\python_file_read.txt") as f:
    seen = set()
    count = 1
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line, end="")
            count += 1
        else:
            seen.add(line_lower)

    print(count)

#****************************************************************
#****************************************************************
"""
import filecmp

file1 = open("D:\Python\FIle_hand\compare_file\File_1.txt")
file2 = open("D:\Python\FIle_hand\compare_file\File_2.txt")
f1 = file1.readline()
f2 = file2.readline()

line = []
for x, y in zip(sorted(file1), sorted(file2)):
    if x == y:
        line.append(x)
    print(x, y)

line = '\n'.join(line)
print(f1, line)

