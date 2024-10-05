import array
import random

def main():
    N = int(input("enter (N): "))
    a = int(input("enter (a): "))
    b = int(input("enter (b): "))
    
    
    first_array = array.array('i', [random.randint(a, b) for _ in range(N)])
    
    
    second_array = array.array('i', [3 ** i for i in range(N)])
    
    
    first_array.extend(second_array)
    
 
    first_array = array.array('i', sorted(first_array))
    
    
    print("result:", first_array)

if __name__ == "__main__":
    main()

