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
constructTriangle = parse_infile("small_triangle.txt")

res = []


res = [[0 for i in range(len(row))] for row in constructTriangle]
res[0][0] = constructTriangle[0][0]
for i in range(1, len(constructTriangle)):
    for j in range(len(constructTriangle[i])):
        if j == 0:
            res[i][j] = res[i-1][j] + constructTriangle[i][j]
        elif j == len(constructTriangle[i])-1:
            res[i][j] = res[i-1][j-1] + constructTriangle[i][j]
        else:
            res[i][j] = min(res[i-1][j-1], res[i-1][j]) + constructTriangle[i][j]
print(min(res[-1]))
print(res)

val = []
#val.append(res[0][0])
i=0
j=0
#temp = 0
for i in range(len(res)):
    #j = temp
    while j < (len(res[i])):
        #j = temp
        if len(res[i])==1:
            val.append(res[i][j])
            #print('Inside if'+res[i][j])
        elif j+1 < len(res[i]):
            val.append(min(res[i][j] - res[i-1][j],res[i][j+1] - res[i-1][j]))
            if (res[i][j+1] - res[i-1][j]) < (res[i][j] - res[i-1][j]):
                j = j+1
            #print(res[i][j] - res[i-1][j])
            #i = i+1
            #temp = j
        break
        #else:
         #   val.append(res[i][j] - res[i-1][j])
        #print(res[i+1][j])
print(val)
#print(res[2][1])
#f = [0] * (len(constructTriangle) + 1)
#for row in constructTriangle[::-1]:
#    for i in range(len(row)):
#        f[i] = row[i] + min(f[i], f[i + 1])
#print(f[0])
#print(f)
#dp = constructTriangle[-1][:]
#print(dp)
#min_path = path_traverse(constructTriangle)
#dp = triangle[-1][:]
#for i in range(len(constructTriangle)-2, -1, -1):
#    for j in range(i+1):
#        dp[j] = min(dp[j], dp[j+1]) + constructTriangle[i][j]
#print(dp[0])
#for i in range(-1,len(constructTriangle)):
#    for j in range(i+1):
#        print(dp[i+j])
   # print('\n')
#print(dp)
#print(min_path)
#print(res)


