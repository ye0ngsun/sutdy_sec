str = input()
a = "_"
for i in str:
    if i == i.upper():
        i = i.lower()
        a += i
    else:
        i = i.upper()
        a += i
print(a[1:])