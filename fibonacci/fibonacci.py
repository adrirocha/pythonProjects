
def fibonacci(num):
    if num < 0:
        raise ('Num must be a positive integer')
    if num == 0:
        return []
    
    res = []
    prev, curr = 1, 1
    prox = 0
    for i in range(num):
        curr += prev
        prev = curr - prev
        prox = curr + prev
        
    res.append(prev)
    res.append(curr)
    res.append(prox)

    return res

x = fibonacci(11)
print(f"Previous: {x[0]}, Currently: {x[1]}, Next: {x[2]}")


