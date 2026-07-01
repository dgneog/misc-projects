# In The Sound of Music, there’s a song sung largely in English, So Long, Farewell wherein “adieu” means “goodbye” in French.
# This program uses inflect library and takes user input as names to make similar lyrics with proper punctuations.

import inflect

names= []

while True:
    try:
        name= str(input(" "))
        names.append(name)
    except EOFError:
        break
    except TypeError:
        pass

for i in range (len(names)):
    p = inflect.engine()
    nameIndex= names[0:i+1]
    subject= p.join(nameIndex)
    print (f"Adieu, adieu, to {subject}")
    i+=1
