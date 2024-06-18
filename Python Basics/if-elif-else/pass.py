def to_be_defined():
    pass
to_be_defined()


try:
    x = 1/0
except ZeroDivisionError:
    pass
print("The script continues")


if True: pass 
else: 
    print("False")