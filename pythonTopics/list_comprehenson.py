lst1=[]
def lst_square(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1
print(lst_square([1,2,3,4]))

lst=[2,3,4,5,6,7,8]
k=[i*i for i in lst if i%2==0]
print(k)