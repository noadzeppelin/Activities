import numpy as np

a1 = np.array([[1,2,3],[4,5,6]])
print(a1)

d = np.empty(3)
print("d ...", d)

e = np.arange(5)
print("e =", e)

f = np.arange(2, 9, 2)
print("f ...",  f)

g = np.linspace(0, 14, num=5)
print("Array g ...", g)

h = np.ones(2, dtype=np.int64)
print(h)

aArray = np.array([[1,2,3,4,5,6,7,8], [11,12,23,34,45,56,67,78]])
print("aArray original ...\n", aArray)

newShape3 = aArray.reshape(4,-1) # try with (8, -1)
print("\naArray reshaped with (4,-1) ...\n", newShape3)

# Sorting an array of strings alphabetically:
arr3 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr3))

arr2 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr2))

arrayone = np.array([3, 0, 9, 12, 6])
sortarray = np.sort(arrayone)
revarray = sortarray[::-1]
print(revarray)

# using NumPy `lexsort()`
colA = [2,1,1,8,1] # First column
colB = [9,0,3,2,0] # Second column
colC = [19,11,11,12,30] #  column

# Sort by colA and then by colC, then by colB
sorted_index = np.lexsort((colB, colC, colA))
print(sorted_index)

#print the result showing the column values as pairs
listAB = [(colA[i],colB[i]) for i in sorted_index]
print("\nCombined column values by index list ...\n", listAB)

# FOLLOW ALONG: lexsort()
first_names = ('George', 'Abraham', 'Denzel')
surnames =    ('Washington',    'Lincoln', 'Washington')

### NOTES: lexsort()
ind = np.lexsort((first_names, surnames))
print(ind)
sorted_names = [surnames[i] + ", " + first_names[i] for i in ind]
print(sorted_names)

# FOLLOW ALONG: Unpacking Notice that there are 3 different arrays, each with 2 separate arrays inside
tt = ([ [ [0, 1, 2, 3], [4, 5, 6, 7] ],
        [ [10, 11, 12, 13], [14, 15, 16, 17] ],
        [[20, 21, 22, 23], [24, 25, 26, 27] ] ])
#this multi-variable assigning method is assigning each main array to the 3 variables
a, b, c = tt

print("a = ", a)
print("b = ", b)
print("c = ", c)
print("The data type of c ...", type(c))

# further unpack the "a" variable
a0, a1 = a
print("\nFurther unpacking a ...")
print("a0 = ", a0)
print("a1 = ", a1)
print("The data type of a1 ...", type(a1))

#Iniating nested array
example = ([ [ [0, 1, 2, 3], [14, 15, 16, 17] ],
        [ [20, 21, 22, 23], [34, 35, 36, 37] ],
        [[40 ,41 ,42, 43], [54, 55, 56, 57] ] ])

#assigning variables to each item in the nested array for easier access to the array
[[[a,b,c,d], [e,f,g,h]],
    [[i,j,k,l],[m,n,o,p]],
    [[q,r,s,t],[u,v,w,x]]] = example

print("1st group ...", a, b, c, d)
print("2nd group ...", m, n, o, p)
print("last bunch ...", q, r, s, t, u, v, w, x)

# Using the '*' to assign all variables that were not assigned
[[[aa,bb,cc,dd], [ee,ff,gg,hh]], *zz] = example

print("\nThe variables aa, bb, to hh ...")
print(aa,bb,cc,dd,ee,ff,gg, hh)

print("\nThe collective variable zz ...")
print(zz)

# Initializing the arrays, and converting them to float values
arr = np.arange(12, dtype = np.float_).reshape(3, 4)
arr1 = np.array([6, 12, 15, 18])
print("arr ...\n", arr)
print("\narr1 ...\n", arr1)

# Example 1: Adding the two arrays
arr2 = np.add(arr, arr1)
print("\nAddition ...\n", arr2)
print(arr2.shape)
print(arr1.shape)

### NOTES: comparison operations
data2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\ndata2 original array ...", data2)
# find all elements < 5
print("data2 elements < 5 ...", data2[data2 < 5])

# find all elements >= 5
five_up = data2 >= 5
print("data2 elements >= 5 ...", data2[five_up])

# using modulo, find all elements divisible by 2
divisible_by_2 = data2[data2 % 2 == 0]
print("data2 elements divisible_by_2 ...", divisible_by_2)
