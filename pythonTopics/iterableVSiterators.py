lst=[1,2,3,4,5]
for i in lst:
    print(i)
# i can say that list is iterables as we can iterate through it:
# print(next(lst)) Through error
lst1=(iter(lst))
print(lst1)
print(next(lst1))
for i in lst1:
    print(i)