import sys

#check errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too much arguments")

#print name tags
print("Hello my name is", sys.argv[1])

#for arg in sys.argv[1:]: <------- this can slice off first item in list
    #print("hello,my name is", arg)
