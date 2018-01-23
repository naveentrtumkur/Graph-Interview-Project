from io import open

#function to parse the input file and convert it into list of lists.
def parse_infile(fPath):
    return [[int(i) for i in l.strip('\n').split()] for l in open(fPath,"r").readlines()] 

#logic for traversing and getting minPath
def path_traverse(constructTriangle):
    constructTriangle.reverse()
    results = constructTriangle.pop(0)
    for row in constructTriangle:
        results = find_row(results, row)
   #print(results[0])
    return results[0]

#function to find the smallest value in a particular row.
def find_row(lower, upper):
    res = []
    for i in range(0,len(upper)):
        #print(upper[i])
        res.append(upper[i] + min(lower[i], lower[i+1]))
        print(res)
        #print(upper[i])
        #print(min(lower[i], lower[i+1]))
    #print(res)
    return res

# Read the input file and convert them into lists.
# We are calling the parser logic, travering the
# tree to find min_path and printing the minimum path value calculated.
constructTriangle = parse_infile("triangle.txt")
min_path = path_traverse(constructTriangle)
print(min_path)
#print(res)


