# Missing numbers in a list

n = int(input("Enter n: "))
list1 = []
for i in range(n):
    ele = int(input())
    list1.append(ele)
list2 = list(range(min(list1), max(list1)))
for i in list1:
    if i in list2:
        list2.remove(i)
print(list2)
