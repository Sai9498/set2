s=int(input())
sum=0
t=s
while s>0:
	x=s%10
	sum=sum+x*x*x
	s=s//10
if t==sum:
	print("yes")
else:
	print("no")
