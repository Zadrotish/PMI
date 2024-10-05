def task_3():
    
    metals_density = {}
    
    for _ in range(9):
        metal = input("metal name: ")
        density = float(input(f"metal density {metal}: "))
        metals_density[metal] = density
    
    
    sorted_by_name = dict(sorted(metals_density.items()))
    print("Sorted by name:", sorted_by_name)
    
    
    sorted_by_density = dict(sorted(metals_density.items(), key=lambda x: x[1], reverse=True))
    print("sorted by density:", sorted_by_density)
    
   
    middle_index = len(sorted_by_density) // 2
    middle_metal = list(sorted_by_density.keys())[middle_index]
    print("A metal, that is in the middle of the dictionary by density:", middle_metal)


task_3()


