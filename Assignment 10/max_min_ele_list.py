li = [10, 30,45, 76, 44, 20, 6, 56, 91]
print(li)

max_num = li[0]
min_num = li[0]

for i in li:
    if  i > max_num:
        max_num = i
    if  i < min_num:
        min_num = i

print("Maximum element in list:", max_num)
print("Minumum element in list:", min_num)