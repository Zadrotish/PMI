import array

def task_1():
    N = int(input("enter N: "))
    
    
    divisors = array.array('i', [i for i in range(1, N+1) if N % i == 0])
    print("N:", divisors)
    
   
    max_divisor = max(divisors)
    min_divisor = min(divisors)
    
    divisors.remove(max_divisor)  
    divisors.remove(min_divisor) 
    
    print(f"array without max number({max_divisor}) and min ({min_divisor}):", divisors)



task_1()