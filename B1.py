max=lambda a,b:a if(a>b)else b
max(4,5)
x=lambda a:a+1
print(x(5))
x=lambda a,b,c:a+b+c
print(x(5,6,2))
def add4(x):
    return x+4
list1=[4,6,7,8,9]
list2=list(map(add4,list1))
print(list2)
def starts_with_A(s):
    return s[0]=="A"
fruit=["Apple","banana","pear","Apricot","orange"]
map_object=map(starts_with_A,fruit)
print(list(map_object))
def oddeven(x):
    if x%2==0:
        return True
    else:
        return False
list1=[4,5,6,7,8,9]
evenlist=list(filter(oddeven,list1))
print(evenlist)
def starts_with_A(s):
    return s[0]=="A"
fruit=["Apple","banana","pear","Apricot","orange"]
filter_object=filter(starts_with_A,fruit)
print(list(filter_object))
from functools import reduce
def sum(x,y):
    return x+y
list1=[6,7,8,9]
S=reduce(sum,list1)
print(S)
