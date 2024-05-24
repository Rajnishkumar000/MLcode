def even_odd(n):
    if n%2==0:
        print("The no is even")
    else:
        print("The no is odd")

even_odd(4)

lst=[1,2,3,4]
# NOW TO CHECK EACH ELEMTENT WE HAVE TO ITERATE THE LIST BUT THERE IS SORTCUT
# map(functions,iterables)
list(map(even_odd,lst))