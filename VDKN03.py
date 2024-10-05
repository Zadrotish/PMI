def task_1():
    x = int(input("Enter x: "))
    
    
    A = tuple(x * i for i in range(1, 21))
    print("A:", A)
    
    
    B = A[9:11]  
    print("B:", B)
    
    
    C = A[-3:]  
    print("C:", C)
    
    
    D = A[:4]  
    print("D:", D)

task_1()

