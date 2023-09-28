# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()
#

with open("/Users/jitendra kumar/Downloads/my_file.txt", mode="r") as file:
    score = file.read()
    print(score)
a = int(score)