def task_2():
    
    A = set(range(1, 26))
    print("A:", A)
    
    
    B = {x for x in A if x % 3 == 0}
    
    
    C = A - B
    
    print("B:", B)
    print("C:", C)


task_2()

