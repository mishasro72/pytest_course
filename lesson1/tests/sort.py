lst =['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99']
lst_1 = []
for i in lst:
    i = i.replace("$", "")
    lst_1.append(float(i))
#lst_1 =sorted(lst, reverse=True)
#lst_1 =sorted(lst)
lst_1.sort(reverse=True)

print(lst)
print(lst_1)
