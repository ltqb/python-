def get_s(n):
    is_s=True
    if n==2:
        is_s=False
    for i in range(2,n):
        if n%i==0:
            is_s=True
            break
        else:
            is_s=False
    return is_s

n=input()
for i in range(1,int(n)+1):
    if get_s(i)==False:
        print(i)
