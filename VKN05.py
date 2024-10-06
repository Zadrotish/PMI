def task_3():
   
    firms = {}
    
    
    n = int(input("how many firms you wan`t add? "))
    
    for _ in range(n):
        name = input("enter firm name: ")
        assets = float(input(f"enter firm bodget  {name}: "))
        firms[name] = assets
    
    
    total_assets = sum(firms.values())
    print(f"budget of al firms: {total_assets}")
    
    
    min_firm = min(firms, key=firms.get)
    max_firm = max(firms, key=firms.get)
    
    print(f"firm with min budget: {min_firm} ({firms[min_firm]})")
    print(f"firm with max budget: {max_firm} ({firms[max_firm]})")


task_3()

