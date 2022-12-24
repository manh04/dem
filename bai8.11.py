Python 3.7.7rc1 (v3.7.7rc1:93b7677f9c, Mar  4 2020, 02:47:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=-10
>>> int_num=x
>>> abs(x)
10
>>> n=int(4)
>>> x=float(5)
>>> s=(x*X + 1)**n
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s=(x*X + 1)**n
NameError: name 'X' is not defined
>>> n=int(4)
>>> x=float(5)
>>> s=(x*x + 1)**n
>>> print("s=", s)
s= 456976.0
>>> n=int(3)
>>> x=float(4)
>>> A=(x*x+x+1)**n+(x*x-x+1)**n
>>> print("A=",A)
A= 11458.0
>>> 