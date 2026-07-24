# You are given runs scored in each over of a T20 innings.
# Build an integer array and print the stats.
# Sample Test Case:
# Input:  [6, 12, 4, 0, 15, 8, 3, 20]
# Output:
# Total runs      : 68
# Highest over    : 20
# Lowest over     : 0
# Average per over: 8.5
# Maiden overs    : 1
# Bytes used      : 32
import array as arr
runs=arr.array('i',map(int,input("Enter the runs Scoored in each over of T20 innings : ").split(' ')))
print("Total runs : ",sum(runs))
print("Highest over : ",max(runs))
print("Lowest over : ",min(runs))
print("Average per over : ",(sum(runs)/len(runs)))
print("Maiden overs : ",runs.count(0))
print("Bytes used : ",runs.itemsize*len(runs))
