n = int(input())
binary = 0
i=1
while(n!=0):
    last_int = int(n%2)
    binary = binary + last_int*i
    n = n/2
    i = i * 10
binary = str(binary)
binary = list(binary)
binary = binary[::-1]
for i in range(0,len(binary)):
    if int(binary[i])==1:
        print(i+1)
        break
