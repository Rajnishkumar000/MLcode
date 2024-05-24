try:
    a=b
    a=2
    b=0
    c=a//b
except NameError as ex:
    print(ex)# shows the message exactly which should be shown in console during error
    print(ex.args)
    print("NameError Exception")

except Exception as ex:
    print(ex)# shows the message exactly which should be shown in console during error
    print(ex.args)
else:
    print("successfully executed")
finally:
    print("This will be executed anyhow")