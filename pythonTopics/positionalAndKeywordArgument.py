def hello(name,age=18):
    print(f'my name is {name} and my age is {age}')
    print('my name is {} and my age is {}'.format(name,age))
hello('Rajnish')

# HERE NAME IS POSTIONAL ARGUMENT
# AND AGE IS KEYWORD ARGUMENT AS IT HAS SOME VALUE ASSIGNED AS DEFAULT

def hi(*args,**kwargs):
    print(args)
    print(kwargs)


hi("Rajnish","Kumar",age=20,dob=2002)

lst=['Rajnish', 'Kumar']
dic={'age': 20, 'dob': 2002}
hi(lst,dic)#by default both are taking as args
# so to overcome this we will use
hi(*lst,**dic)

# HERE ARGS IS POSITIONAL ARGS AND KWARGS IS KEYWORD ARGS

# we can return multiple values from a function