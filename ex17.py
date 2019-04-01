from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# We could do these two in one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CRTL-C to abort")
input()
# First parameter is the file name, second parameter determines the mode in which we want to allow file to open
# – If you want to read the file, pass in r
# – If you want to read and write the file, pass in r+
# – If you want to overwrite the file, pass in w
# – If you want to append to the file, pass in a
out_file= open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()