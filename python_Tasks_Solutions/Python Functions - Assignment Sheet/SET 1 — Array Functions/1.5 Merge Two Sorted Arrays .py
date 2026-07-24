#Merge two already-sorted arrays into one sorted array — without using sorted().
#Input:  a = [1, 4, 7, 9],  b = [2, 3, 8, 10, 15]
#Output: [1, 2, 3, 4, 7, 8, 9, 10, 15]
import array as arr
nums1=arr.array('i',map(int,input('Enter elements in first array: ').split(' ' )))
nums2=arr.array('i',map(int,input('Enter elements in seconds array : ').split(' ')))
i,j,n1,n2=0,0,len(nums1),len(nums2)
res=[]
while i<n1 and j<n2:
    if nums1[i]<=nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j+=1
while i<n1:
    res.append(nums1[i])
    i+=1
while j<n2:
    res.append(nums2[j])
    j+=1
print('Merge 2 sorted array',res)
