










def file_summator(input_file="", current_number=0):
    in_file = open(input_file, "r")
    total = current_number
    for line in in_file:
        total += int(line)
    return(total)



# input_file = open("input.txt", "r")

# # print(input_file.read())

# # for line in input_file.read():
# #     print (line)


# current_number = 0

# for line in input_file:
#     # print (line)
#     # print(int(line))
#     current_number += int(line)
# 
# print(current_number)
# return(current_number)

print(file_summator("input.txt", 0))
