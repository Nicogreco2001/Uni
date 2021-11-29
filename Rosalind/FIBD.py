
def fibonacci_of(n,k):
    cache = {0: 0, 1: 1} 
    if n in cache:       
        return cache[n]  
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2) 
    return cache[n]
   
n = int(input())
ll = [fibonacci_of(x) for x in range(n)]
print(*ll)