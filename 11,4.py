lst = []
while True:
    a = int(input('nhập giá trị :'))
    hoi = input('(tiếp tục nhập giá trị?(1/0):')
    lst.insert(0,a)
    if hoi == '0':
        lst.reverse()
        print('list:',lst)
        break
x =int(input('nhập vào số x:'))
#tổng list
sum = 0
for num in lst:
    sum += num
print(sum)
y = lst.count(x)
print(x,'xuất hiện ',y,'lần trong list')
d=0
for i in lst:
    if x<i:
        d+=1
if d==(len(lst)-1):
    print(x," không lớn hơn tất cả số trong list")
else:
    print(x," lớn nhỏ hơn số một vài số trong list")
print('các số lớn hơn 5 trong list là ')
for j in range(len(lst)):
    if x<lst[j]:
        print(lst[j],end=" ")