list1 = [1, 2, 3],[11, 22, 33]
list2 = [4, 5]
for (a, b) in zip(list1, list2):   #list1,list2を同時にループ
    print(a,b)



list1 = [1, 2, 3],[4, 5, 6],[7, 8, 9]
list2 = [11, 22, 33],[44, 55, 66],[77, 88, 99]
list1[1:] += list2[1:]
print(list1)




import numpy as np
list8 = np.array([1, 2, 3])
list9 = np.array([11, 22, 3])
list8 += list9
print(list8)



list1 = [1, 2, 3]
list2 = [11, 22, 33]
list1[1:] += list2[1:]
print(list1)
