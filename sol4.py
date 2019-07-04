num = list(map(int, input().split()))
for i in range(num[0]+1, num[-1]):
  if i % 2 != 0:
    print(i, end=" ")
