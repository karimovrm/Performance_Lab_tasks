with open('circle.txt', 'r') as file1:
    a, b, r = map(int, file1.read().split())

with open('dot.txt', 'r') as file2:
    s = map(lambda x: x.strip().split(), file2.readlines())
    for i in s:
        x, y = map(int, i)
        if (x - a) ** 2 + (y - b) ** 2 < r ** 2:
            print(1, end='\n')
        elif (x - a) ** 2 + (y - b) ** 2 > r ** 2:
            print(2, end='\n')
        else:
            print(0, end='\n')

