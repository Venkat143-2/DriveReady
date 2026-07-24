#Start with array('i',[10, 20, 30, 40, 50]) and apply these operations in order.
#Print the array after each step.
#Operations:
#  1. append 60
#  2. insert 15 at index 1
#  3. remove the value 30
#  4. pop the element at index 0
#  5. reverse
#
#Output:
#After append  : array('i', [10, 20, 30, 40, 50, 60])
#After insert  : array('i', [10, 15, 20, 30, 40, 50, 60])
#After remove  : array('i', [10, 15, 20, 40, 50, 60])
#After pop     : array('i', [15, 20, 40, 50, 60])  (popped 10)
#After reverse : array('i', [60, 50, 40, 20, 15])
import array as arr
patient=arr.array('i',map(int,input('Enter Elements : ').split(' ')))
patient.append(60)
print('After Append Operation :',patient)
patient.insert(1,15)
print('After Insertion Operation :',patient)
patient.remove(30)
print('After Remove Operation :',patient)
popped_element=patient.pop(0)
print('After Pop Operation :',patient,'popped',popped_element)
patient.reverse()
print('After Reverse Operation :',patient)
