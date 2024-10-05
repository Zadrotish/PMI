import numpy as np
import math

def main():
    N = int(input("enter N: "))
    
    
    sqrt_N = math.isqrt(N)
    if sqrt_N ** 2 != N:
        N = (sqrt_N + 1) ** 2
        print(f"number is not correct square, up to {N}")
    else:
        print(f"number is correct square: {N}")
    
    
    size = math.isqrt(N)
    
    
    A = np.arange(1, N+1).reshape(size, size)
    
   
    print("A:")
    print(A)

if __name__ == "__main__":
    main()

