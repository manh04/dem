
n=int(input("nhập số n="))
flag=True
if n<2:
    print(n, "không nguyên tố")
else:
    for i in range(2, int(n/2)):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")