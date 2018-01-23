# @author Naveen Tumkur Ramesh Babu
##################################
# Minimum Path Traversal Program #
##################################

# Given a triangle of numbers, find the valid path that generates the minimum sum possible
# starting at the top of the triangle and moving to adjacent numbers in the row below
# until you reach the bottom. 


# Import this to handle file operations.
import sys
from io import open


#function to parse the input file and convert it into list of lists.
# This would be used as input for our program.
def parse_infile(fPath):
    return [[int(i) for i in l.strip('\n').split()] for l in open(fPath,"r").readlines()] 

# Read the input file and convert them into lists.
# We are calling the parser logic, travering the
# tree to find min_path and printing the minimum path value calculated.


def main():
    filen = sys.argv[1]
    constructTriangle = parse_infile(filen)

    # I'm using Dynamic programming to approach this problem.
    # I'm using a top-down approach to solve this problem.
    # Using a res, I will be avoiding overlapping subproblems.
    # Create a res list initialized to 0.
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
    # Outputs the final value of the minimum sum of path traversal.
    #print(min(res[-1]))
    #print(res)

    # The path traversal value would be stored in val and printed out at last.
    val = []

    # Initialise variables i and j to zero.
    i=0
    j=0

    # Update the list-val with the path traversal values.
    for i in range(len(res)):
        while j < (len(res[i])):
            if len(res[i])==1:
                val.append(res[i][j])
            elif j+1 < len(res[i]):
                val.append(min(res[i][j] - res[i-1][j],res[i][j+1] - res[i-1][j]))
                if (res[i][j+1] - res[i-1][j]) < (res[i][j] - res[i-1][j]):
                     j = j+1
            break
            #else:
            #  val.append(res[i][j] - res[i-1][j])
            #print(res[i+1][j])
    #print(val)

    # Print the path traversal nodes to the output.
    for i in val:
        print(i)

if __name__ == '__main__':
    main()
###################################################### END OF THE PROGRAM #################################
