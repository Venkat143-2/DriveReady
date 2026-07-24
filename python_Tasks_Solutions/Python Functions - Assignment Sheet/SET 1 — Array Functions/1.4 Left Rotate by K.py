#Rotate an array to the left by k positions.
#Input:  arr = [1, 2, 3, 4, 5, 6, 7],  k = 3
#Output: [4, 5, 6, 7, 1, 2, 3]
#Input:  arr = [1, 2, 3],  k = 5
#Output: [3, 1, 2]
#k can be bigger than the array length. Handle it.
import array as arr
sorted_array=arr.array('i',map(int,input('Enter Elements : ').split(' ')))
k=int(input('Enter no of left rotations to roatate the array : '))
rotations=k%len(sorted_array)
rotated_array=sorted_array[rotations:]
rotated_array.extend(sorted_array[:rotations])
print(f"After {k} rotations the array is {rotated_array.tolist()}")
