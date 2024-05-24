# also called as anonymous function
# works faster
# also called a function with no name

def add(a,b):
    return a+b
print(add(2,3))


# USING lambda
sum=lambda a,b:a+b
a=sum(2,6)
print(a)

even=lambda n:n%2==0
print(even(2))