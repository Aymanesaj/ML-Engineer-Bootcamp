import sys

if len(sys.argv) == 1:
    sys.exit(1)
try:
    assert not len(sys.argv) > 2, "Too many arguments"
    assert sys.argv[1].isdigit(), "argument is not an integer"
except AssertionError as msg:
    print(msg)
    sys.exit(1)

num = int(sys.argv[1])
if num == 0:
    print("I'm Zero.")
elif num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")