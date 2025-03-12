import sys

if len(sys.argv) < 2:
    sys.exit(1)

input_string = " ".join(sys.argv[1:])
output_string = input_string[::-1].swapcase()

print(output_string)