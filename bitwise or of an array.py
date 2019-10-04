N = int(input())
mylist = list(map(int,input().split()[:N]))
result = mylist[0]
for i in range(0,N):
    result = result | mylist[i]
print(result)
