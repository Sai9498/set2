numbr = list(map(int, input().split()))
for i in range(numbr[0]+1, numbr[-1]):
  if i % 2 != 0:
    print(i, end=" ")
