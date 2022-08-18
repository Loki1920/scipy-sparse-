import numpy as np
from scipy.sparse import csr_matrix

# create csr matrix from an array
arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

#Viewing stored data (not the zero items) with the data property:
arr1 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr1).data)
# count non zero 
print(csr_matrix(arr1).count_nonzero())

#Removing zero-entries from the matrix with the eliminate_zeros() method:
mat = csr_matrix(arr1)
mat.eliminate_zeros()
print(mat)
# remove duplicate value using sum_duplicates()
print("sum_duplicates() method ")
mat.sum_duplicates()
print(mat)

# coverting csr to csc matrix
print("csr to csc")
new_arr = csr_matrix(arr1).tocsc()
print(new_arr)