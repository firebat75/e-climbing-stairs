
def climbStairs(n: int) -> int:
    
    if n == 0:
        return 0
    
    selections = [[1], [2]]
    
    prev = 2
    
    for i in range(n):
        
        count = 0
        
        for e in range(prev):
            
            selections += [selections[-(prev)] + [1]]
            selections += [selections[-(prev) - 1] + [2]]
            
            prev += 1
            count += 2
        
        prev = count

    output = []

    for item in selections:
        if sum(item) == n:
            output.append(item)
        

    return len(output)
        