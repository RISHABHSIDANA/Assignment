t_1 = (1, 4, 9, 16, 25, 36)
t_modified = tuple(x**2 for x in t_1)
print("t_1:", t_1)
print("t_modified:", t_modified)
print("Element at index postiion 4 of t_modified:", t_modified[4])
t_sliced = t_modified[1:4]
print("t_sliced:", t_sliced)
