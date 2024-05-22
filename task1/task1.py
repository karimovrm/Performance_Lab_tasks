n, m = int(input()), int(input())

list1 = m * [i for i in range(1, n + 1)]
list2 = [0]
list3 = []
cnt = 0

while list2[-1] != 1:
    list2.clear()
    for i in range(cnt, m + cnt):
        list2.append(list1[i])
        cnt += 1
    list2_copy = list2.copy()
    list3.append(list2_copy)
    cnt -= 1
for i in range(len(list3)):
    print(list3[i][0], end='')
