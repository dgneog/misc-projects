## This program takes a system argument being the file name in the folder along with its .py and finds the lines of code.
# If the extension of the file isn't ".py", the programs outputs a non-zero system error

import sys
i=0

if len(sys.argv)==2:
    file,extension= sys.argv[1].split(".")
    if extension=="py":
        with open(f"{sys.argv[1]}") as file:
            lines= file.readlines()
        for line in lines:
            if line.strip()!="" and not line.strip().startswith("#"):
                i+=1
    else:
        print ("Not a Python file")
        sys.exit(1)
elif len(sys.argv)>2:
    print ("Too many command-line arguments")
    sys.exit(1)

else:
    print ("Too few command-line arguments")
    sys.exit(1)

print (i)
