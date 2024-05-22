with open('numbers.txt', 'r') as file:
    s = [int(i.strip()) for i in file.readlines()]


s.sort()
middle = s[len(s)//2]
result = [abs(i - middle) for i in s]
print(sum(result))