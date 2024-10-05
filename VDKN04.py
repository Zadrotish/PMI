
def task_2():
    
    K = {i for i in range(-34, 45) if str(i).endswith('4')}
    print("K:", K)
    
    
    K = {i for i in K if i % 4 != 0}
    print("K after removing numbers divisible by 4:", K)


task_2()
