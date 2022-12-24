import math
a=float(input("Nhập cân nặng(kg):" ))
b=float(input("Nhập chiều cao(m):"))
BMI=a/(b*b)
print("chỉ số BMI của bạn là:",BMI)
if BMI<18.5:
    print("Bạn gầy quá")
elif BMI <=25:
    print("Cơ thể của bạn bình thường")
elif BMI>=25:
    print("Bạn bị thừa cân")