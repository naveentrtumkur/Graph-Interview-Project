/******************************************************* 
 * Minimum Path Traversal Program using Python3.
 *
 * Given a triangle of numbers, find the valid path that generates the minimum sum possible starting at th etop of the triangle
 * and moving to adjacent numbers in the row below until you reach the bottom.
 *
 *     62
 *   44 93
 *  96 16 38
 * 72 58 98 26
 *
 * For example, in the above triangle, the minimal path is 62 -> 44 -> 16 -> 58 which sums to 180. (Edges have been removed for clarity.) 
 *
 * Sample Output Format:
 * (proj) Naveens-MacBook-Pro:Graph-Interview-Project naveentr$ python3 traversal.py small_triangle.txt 
 *  79
 *  4
 *  64
 *  17
 *  33
 *  26
 *  30
 *  72
 *  37
 *  25
 *
 * I have used Dynamic Programming to solve this problem.
 * I haven't used any additional library except sys and io.
 *
 * -> I have checked my output by verfiying teh answer for min Path Sum for small input and manually solving and verifying the output.
 * -> I have checked that the minimum path sum matches for the large input file.
 *
 *
 *********************************************************/




