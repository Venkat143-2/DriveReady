# Find the second largest element without using sort() or sorted().
# Input:  [45, 88, 12, 88, 67, 90]
# Output: Second largest = 88
# Input:  [5, 5, 5]
# Output: No second largest
# Careful: [45, 88, 12, 88, 67, 90] — the largest is 90, so the second largest is 88, even though 88 appears twice.
import array as arr
scores=arr.array('i',map(int,input('Enter the scores : ').split(' ')))
First_largest=float('-inf')
second_largest=float('-inf')
for i in scores:
    if i>First_largest:
        Second_largest,First_largest=First_largest,i
    elif i>Second_largest:
        Second_Largest=i
if Second_largest!=float('-inf'):
    print('Second Largest :',Second_largest)
else:
    print('No Second Largest')
