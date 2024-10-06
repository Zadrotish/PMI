import numpy as np

def task_2():
    N = int(input("enter matrix N: "))
    
   
    matrix = np.random.randint(1, 13, size=(N, N))
    print("matrix:")
    print(matrix)
    
    
    diagonal_product = np.prod(np.diagonal(matrix))
    print("Product of elements on the main diagonal:", diagonal_product)
    
    
    unique_elements = set()
    for i in range(N):
        for j in range(N):
            if matrix[i, j] in unique_elements:
                matrix[i, j] = 0
            else:
                unique_elements.add(matrix[i, j])
    
    print("matrix without repits (instead of repeats 0):")
    print(matrix)


task_2()

