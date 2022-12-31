def so_may_man(x):
    if x%7==0:
        return True
    else:
        return False
a = list(eval(input("Nhập các phần tử của danh sách trên một dòng và cách nhau bởi DẤU PHẨY: ")))
d=0
for i in a:
    if so_may_man(i):
        d+=1
if d>=1:
    print("True")
else:
    print('False')
