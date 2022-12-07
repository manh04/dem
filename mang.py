a=[]
m=int(input())
n=int(input())
for i in range(m):
    print("Chuẩn bị nhập ma trận thứ ",i+1,":")
    b=[]
    for j in range(n):
        x=int(input("Nhập phần tử thứ:"+str(j+1)+":"))
        b=b+[x]
    a.append(b)
    print("Ma trận A đã nhập xong!")    
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
