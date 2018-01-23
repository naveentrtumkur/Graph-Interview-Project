

#def parse_infile("triangle.txt"):
obj= [[int(i) for i in l.strip('\n').split()] for l in open("small_triangle.txt","r").readlines()]
print(obj)

i=0
with open("nav.txt",'w') as f:
    f.write("[")
    for item in obj:
        i = i+1
        f.write("{}".format(item))
        # To get teh count of items to be written and get the count.
        if(i<len(obj)):
            f.write(",")
    f.write("]")

#for item in obj:
#    f.write("%s",%item)
f.close()
