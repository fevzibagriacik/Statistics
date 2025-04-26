def shifted(array):
    sum = 0
    n = len(array)
    sorted(array)

    for i in array:
        sum += i
    
    mean = sum / n
        
    if n % 2 == 0:
        median = (array[n // 2] + array[(n // 2) - 1]) / 2
    else:
        median = (array[n // 2])
        
    if median > mean:
        diff = ((median - mean) / mean) * 100
    else:
        diff = ((mean - median) / median) * 100

    return diff
    
    
